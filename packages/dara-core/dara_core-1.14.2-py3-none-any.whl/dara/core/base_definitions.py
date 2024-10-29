"""
Copyright 2023 Impulse Innovations Limited


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations

# This file should be used for an definitions that have no deps at all so that they can always be imported and shared
# between other parts of the framework
import abc
import uuid
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    ClassVar,
    List,
    Mapping,
    Optional,
    Union,
)

import anyio
from anyio.streams.memory import MemoryObjectSendStream
from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from dara.core.interactivity.actions import ActionCtx


class DaraBaseModel(BaseModel):
    """
    Custom BaseModel which handles TemplateMarkers.
    If TemplateMarkers are present, validation is skipped.
    """

    class Config:
        smart_union = True
        extra = 'forbid'

    def __init__(self, *args, **kwargs):
        has_template_var_marker = any(isinstance(arg, TemplateMarker) for arg in args) or any(
            isinstance(value, TemplateMarker) for value in kwargs.values()
        )

        if has_template_var_marker:
            # Imitate pydantic's BaseModel.__init__ but avoid validation
            values = {}
            fields_set = set()
            _missing = object()

            for name, field in self.__class__.__fields__.items():
                value = kwargs.get(field.alias, _missing)
                if value is _missing:
                    value = field.get_default()
                else:
                    fields_set.add(name)
                values[name] = value

            object.__setattr__(self, '__dict__', values)
            object.__setattr__(self, '__fields_set__', fields_set)
            self._init_private_attributes()
        else:
            super().__init__(*args, **kwargs)


class CacheType(str, Enum):
    """Cache types enum"""

    GLOBAL = 'global'
    SESSION = 'session'
    USER = 'user'

    @classmethod
    def get_member(cls, value: str):
        """
        Get a member of the enum by value
        """
        try:
            return cls(value)
        except ValueError:
            return None


class BaseCachePolicy(BaseModel, abc.ABC):
    """
    Base class for cache policies.
    """

    policy: str
    cache_type: CacheType = CacheType.GLOBAL


class LruCachePolicy(BaseCachePolicy):
    """
    Least-recently-used cache policy.
    Evicts the least recently used item when adding a new item to the cache if the number of items
    exceeds the max_size.

    :param max_size: maximum number of items to keep in the cache - globally or per user/session,
        depending on `cache_type` set in the policy
    """

    policy: str = Field(const=True, default='lru')
    max_size: int = 10


class MostRecentCachePolicy(LruCachePolicy):
    """
    Most recent cache policy. Only keeps the most recent item in the cache.
    """

    policy: str = Field(const=True, default='most-recent')
    max_size: int = Field(const=True, default=1)


class KeepAllCachePolicy(BaseCachePolicy):
    """
    Keep all items in the cache, regardless of the number of items.

    Should be used with caution as it can lead to memory leaks.
    """

    policy: str = Field(const=True, default='keep-all')


class TTLCachePolicy(BaseCachePolicy):
    """
    Time-to-live cache policy.
    Evicts items from the cache after the specified time-to-live.

    :param ttl: time-to-live in seconds
    """

    policy: str = Field(const=True, default='ttl')
    ttl: int


class Cache:
    """
    Convenience class aggregating all available cache policies and types
    """

    Type = CacheType

    class Policy:
        """
        Available cache policies
        """

        LRU = LruCachePolicy
        MostRecent = MostRecentCachePolicy
        KeepAll = KeepAllCachePolicy
        TTL = TTLCachePolicy

        @classmethod
        def from_arg(cls, arg: CacheArgType) -> BaseCachePolicy:
            """
            Construct a cache policy from a cache arg. Defaults to LRU if a type is provided.
            """
            if isinstance(arg, BaseCachePolicy):
                return arg

            if isinstance(arg, Cache.Type):
                return LruCachePolicy(cache_type=arg)

            if isinstance(arg, str):
                # Check that the string is one of allowed cache members
                if typ := Cache.Type.get_member(arg):
                    return LruCachePolicy(cache_type=typ)

            raise ValueError(
                f'Invalid cache argument: {arg}. Please provide a Cache.Policy object or one of Cache.Type members'
            )

        @classmethod
        def from_dict(cls, arg: dict) -> Optional[BaseCachePolicy]:
            """
            Construct a cache policy from its serialized dict represetnation
            """
            if arg is None or not isinstance(arg, dict):
                return None

            policy_name = arg.get('policy')

            if policy_name == 'lru':
                return LruCachePolicy(**arg)
            elif policy_name == 'most-recent':
                return MostRecentCachePolicy(**arg)
            elif policy_name == 'keep-all':
                return KeepAllCachePolicy(**arg)
            elif policy_name == 'ttl':
                return TTLCachePolicy(**arg)
            else:
                raise ValueError(f'Invalid cache policy: {arg}')


CacheArgType = Union[CacheType, BaseCachePolicy, str]


class CachedRegistryEntry(BaseModel):
    """
    Represents a registry item with associated cache entries which can be controlled
    via the cache policy.
    """

    cache: Optional[BaseCachePolicy]
    uid: str

    def to_store_key(self):
        """
        Returns a unique store key for this entry.
        """
        return f'{self.__class__.__name__}_{self.uid}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(cache={self.cache}, uid={self.uid})'


class BaseTaskMessage(BaseModel):
    task_id: str


class TaskProgressUpdate(BaseTaskMessage):
    progress: float
    message: str


class TaskResult(BaseTaskMessage):
    result: Any
    cache_key: Optional[str]
    reg_entry: Optional[CachedRegistryEntry]


class TaskError(BaseTaskMessage):
    error: BaseException
    cache_key: Optional[str]
    reg_entry: Optional[CachedRegistryEntry]

    class Config:
        arbitrary_types_allowed = True


TaskMessage = Union[TaskProgressUpdate, TaskResult, TaskError]


class BaseTask(abc.ABC):
    """
    Generic BaseTask that can be used for type checking tasks
    """

    cache_key: Optional[str]
    reg_entry: Optional[CachedRegistryEntry]
    notify_channels: List[str]
    task_id: str

    @abc.abstractmethod
    def __init__(self, task_id: Optional[str] = None) -> None:
        self.task_id = str(uuid.uuid4()) if task_id is None else task_id
        super().__init__()

    @abc.abstractmethod
    async def run(self, send_stream: Optional[MemoryObjectSendStream[TaskMessage]] = None) -> Any:
        ...

    @abc.abstractmethod
    async def cancel(self):
        ...


class PendingTask(BaseTask):
    """
    Represents a running pending task.
    Is associated to an underlying task definition.
    """

    cache_key: None = None
    reg_entry: None = None

    def __init__(self, task_id: str, task_def: BaseTask, ws_channel: Optional[str] = None):
        self.task_id = task_id
        self.task_def = task_def
        self.notify_channels = [ws_channel] if ws_channel else []

        self.cancel_scope: Optional[anyio.CancelScope] = None
        self.event = anyio.Event()
        self.result: Optional[Any] = None
        self.error: Optional[BaseException] = None
        self.subscribers = 1

    async def run(self, send_stream: Optional[MemoryObjectSendStream[TaskMessage]] = None):
        """
        Wait for the task to complete
        """
        # Waiting in chunks as otherwise Jupyter blocks the event loop
        while not self.event.is_set():
            await anyio.sleep(0.01)

        if self.error:
            raise self.error

        return self.result

    def resolve(self, value: Any):
        """
        Resolve the pending state and send values to the waiting code

        :param value: the value to resolve as the result
        """
        self.result = value
        self.event.set()

    def fail(self, exc: BaseException):
        """
        Resolve the pending state with an error and send it to the waiting code

        :param exc: exception to resolve as the result
        """
        self.error = exc
        self.event.set()

    async def cancel(self):
        """
        Stop the task
        """
        if self.cancel_scope:
            self.cancel_scope.cancel()
        await self.task_def.cancel()

        self.error = Exception('Task was cancelled')
        self.event.set()

    def add_subscriber(self):
        """
        Add 1 to the subscriber count
        """
        self.subscribers += 1

    def remove_subscriber(self):
        """
        Remove 1 from the subscriber count
        """
        self.subscribers -= 1


class PendingValue:
    """
    An internal class that's used to represent a pending value. Holds a future object that can be awaited by
    multiple consumers.
    """

    def __init__(self):
        self.event = anyio.Event()
        self._value = None
        self._error = None

    async def wait(self):
        """
        Wait for the underlying event to be set
        """
        # Waiting in chunks as otherwise Jupyter blocks the event loop
        while not self.event.is_set():
            await anyio.sleep(0.01)
        if self._error:
            raise self._error
        return self._value

    def resolve(self, value: Any):
        """
        Resolve the pending state and send values to the waiting code

        :param value: the value to resolve as the result
        """
        self._value = value
        self.event.set()

    def error(self, exc: Exception):
        """
        Resolve the pending state with an error and send it to the waiting code

        :param exc: exception to resolve as the result
        """
        self._error = exc
        self.event.set()


class AnnotatedAction(BaseModel):
    """
    Represents a single call to an @action-annotated action.

    ```python
    from dara.core import action

    @action
    def my_action(ctx: action.Ctx, ...):
        ...

    result = my_action(...)
    type(result) == AnnotatedAction
    ```
    """

    uid: str
    """Instance uid of the action. Used to find static kwargs for the instance"""

    definition_uid: str
    """Uid of the action definition"""

    dynamic_kwargs: Mapping[str, Any]
    """Dynamic kwargs of the action; uid -> variable instance"""

    loading: 'Variable'   # type: ignore
    """Loading Variable instance"""

    def __init__(self, **data):
        # Resolve the circular dependency to add a loading Variable to the model upon creation
        # pylint: disable-next=import-error, import-outside-toplevel
        from dara.core.interactivity.plain_variable import Variable

        self.update_forward_refs(Variable=Variable)
        super().__init__(**data, loading=Variable(False))


class ActionImpl(DaraBaseModel):
    """
    Base class for action implementations

    :param js_module: JS module including the implementation of the action.
    Required for non-local actions which have a JS implementation.
    """

    js_module: ClassVar[Optional[str]] = None
    py_name: ClassVar[Optional[str]] = None

    async def execute(self, ctx: ActionCtx) -> Any:
        """
        Execute the action.

        Default implementation sends the args to the frontend which can be called by subclasses.

        :param context: ActionContext instance
        """
        await ctx._push_action(self)

    def dict(self, *args, **kwargs):
        """
        This structure is expected by the frontend, must match the JS implementation
        """
        dict_form = super().dict(*args, **kwargs)
        dict_form['name'] = self.__class__.py_name or self.__class__.__name__
        dict_form['__typename'] = 'ActionImpl'
        return dict_form


ActionInstance = Union[ActionImpl, AnnotatedAction]
"""
@deprecated alias for backwards compatibility
"""

# TODO: remove List[AnnotatedAction] support in 2.0
Action = Union[ActionImpl, AnnotatedAction, List[Union[AnnotatedAction, ActionImpl]]]
"""
Definition of an action that can be executed by the frontend.
Supports:
- AnnotatedAction: an @action annotated function
- ActionImpl: an instance of a subclass of ActionImpl
- a list of either of the above

@deprecated when passing a list only ActionImpl will be supported in dara 2.0
"""


class ActionDef(BaseModel):
    """
    Action definition required to register actions in the app.
    Links the name of the action with its JS implementation.

    :param name: name of the action, must match the Python definition and JS implementation
    :param py_module: name of the PY module with action definition, used for versioning
    :param js_module: JS module where the action implementation lives.
    Not required for local actions as they are located via dara.config.json
    """

    name: str
    py_module: str
    js_module: Optional[str]


class ActionResolverDef(BaseModel):
    uid: str
    """Unique id of the action definition"""

    resolver: Optional[Callable]
    """Resolver function for the action"""

    execute_action: Callable[..., Awaitable[Any]]
    """Handler to execute the action, default dara.core.internal.execute_action.execute_action"""


class UploadResolverDef(BaseModel):
    resolver: Optional[Callable]
    """Optional custom resolver function for the upload"""
    upload: Callable
    """Upload handling function, default dara.core.interactivity.any_data_variable.upload"""


class ComponentType(Enum):
    """Component types enum"""

    JS = 'js'
    PY = 'py'


class TemplateMarker(BaseModel):
    """
    Template marker used to mark fields that should be replaced with a data field on the client before being rendered.
    See dara_core.definitions.template for details
    """

    field_name: str

    def dict(self, *args, **kwargs):
        dict_form = super().dict(*args, **kwargs)
        dict_form['__typename'] = 'TemplateMarker'
        return dict_form
