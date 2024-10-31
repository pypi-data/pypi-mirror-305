import asyncio
from functools import partial
import inspect
from typing import (
    Callable,
    Literal,
    Optional,
    ParamSpec,
    TypeVar,
    cast,
    overload,
)


from utran.core.backend.base import AbstractConnection
from ..general.exceptions import (
    RemoteNotImplementedError,
)
from ..general.base_action import Action, CacheType, keys


REMOTE_IMP_ACTIONS: dict[str, "RemoteImpAction"] = {}

def _get_all_imp_actions() -> list['RemoteImpAction']:
    """获取所有远程action, 给tots command使用"""
    return list(REMOTE_IMP_ACTIONS.values())

def get_remote_imp_action(action_key: str) -> Optional["RemoteImpAction"]:
    """获取远程实现action"""
    return REMOTE_IMP_ACTIONS.get(action_key)


R = TypeVar("R")
P = ParamSpec("P")


class RemoteImpAction(Action[P, R]):
    """远程实现action"""

    def _pre_init(self, *, action_key: str, source_fn: Callable[..., R]):
        """前置检查 action_key是否合法"""
        for k, v in REMOTE_IMP_ACTIONS.items():
            if k == action_key:
                raise ValueError(f"action_key '{action_key}' already be used by {v}")





_D = TypeVar("_D")


@overload
def register_remote_imp_action(
    fn: Callable[P, R],
    action_key: Optional[str],
    *,
    default_fn: Literal[None] = None,
    timeout: Optional[float] = None,
    **kwargs,
) -> RemoteImpAction[P, R]: ...
@overload
def register_remote_imp_action(
    fn: Callable[P, R],
    action_key: Optional[str],
    *,
    default_fn: Callable[..., _D],
    timeout: Optional[float] = None,
    **kwargs,
) -> RemoteImpAction[P, R|_D]: ...
def register_remote_imp_action(
    fn: Callable[P, R],
    action_key: Optional[str],
    *,
    default_fn: Callable[..., _D] | None=None,
    timeout: Optional[float] = None,
    **kwargs,
) -> RemoteImpAction[P, R] | RemoteImpAction[P, R|_D]:
    """
    添加远程实现action函数
    - fn: 远程实现函数
    - action_key: 远端实现的action名称,默认为函数名称
    - default_fn: 默认函数,当远端无可调用实现时调用,默认为None
    - timeout: 远端调用超时时间,默认为None,不超时
    - **kwargs: 其他参数
    """

    action_key = fn.__name__ if action_key is None else action_key

    if ac := get_remote_imp_action(action_key):
        ac.check_signatures(fn)
        return ac

    from utran.core.host import __CONNECTIONS__
    from utran.core.ipc import async_remote_call, sync_remote_call

    if asyncio.iscoroutinefunction(fn):

        async def async_wrapper(*args, **kw):
            """异步函数远程调用目标Action"""
            target_conns: AbstractConnection | None = None

            for conn in __CONNECTIONS__.values():
                if action_key in conn.imp_ations:
                    target_conns = conn
                    break

            if target_conns is None:
                if default_fn is None:
                    raise RemoteNotImplementedError(f"'{action_key}',远端无可调用实现")
                else:
                    return default_fn(*args, **kw)

            return await async_remote_call(
                target_conns,
                action_key,
                params=dict(args=args, kwargs=kw),
                timeout=timeout,
            )

        impAction = RemoteImpAction(async_wrapper, action_key, source_fn=fn, **kwargs)

    else:

        def wrapper(*args, **kw):
            """同步函数远程调用目标Action"""
            target_conns: AbstractConnection | None = None

            for conn in __CONNECTIONS__.values():
                if action_key in conn.imp_ations:
                    target_conns = conn
                    break

            if target_conns is None:
                if default_fn is None:
                    raise RemoteNotImplementedError(f"'{action_key}',远端无可调用实现")
                else:
                    return default_fn(*args, **kw)

            return sync_remote_call(
                target_conns,
                action_key,
                params=dict(args=args, kwargs=kw),
                timeout=timeout,
            )

        impAction = RemoteImpAction(wrapper, action_key, source_fn=fn, **kwargs)

    REMOTE_IMP_ACTIONS[action_key] = impAction
    return cast(RemoteImpAction[P, R], impAction)


@overload
def remote_imp(
    _: Callable[P, R],
    *,
    action_key: Optional[str] = None,
    default_fn: Literal[None] = None,
    cache: CacheType = None,
    cache_key_func: Callable = keys.hashkey,
    lock=False,
    timeout: Optional[float] = None,
) -> RemoteImpAction[P, R]: ...
@overload
def remote_imp(
    *args,
    action_key: Optional[str] = None,
    default_fn: Literal[None] = None,
    cache: CacheType = None,
    cache_key_func: Callable = keys.hashkey,
    lock=False,
    timeout: Optional[float] = None,
) -> Callable[[Callable[P, R]], RemoteImpAction[P, R]]: ...
@overload
def remote_imp(
    *args,
    action_key: Optional[str] = None,
    default_fn: Callable[..., _D],
    cache: CacheType = None,
    cache_key_func: Callable = keys.hashkey,
    lock=False,
    timeout: Optional[float] = None,
) -> Callable[[Callable[P, R]], RemoteImpAction[P, R|_D]]: ...
def remote_imp(
    *args,
    _: Callable[P, R]|None = None,
    action_key: Optional[str] = None,
    default_fn: Callable[..., _D] | None=None,
    cache: CacheType = None,
    cache_key_func: Callable = keys.hashkey,
    lock=False,
    timeout: Optional[float] = None,
)-> Callable[[Callable[P, R]], RemoteImpAction[P, R]|RemoteImpAction[P, R|_D]]|RemoteImpAction[P, R]:
    """### 装饰器,将函数注册到REMOTE_IMP_ACTIONS中
    - action_key: 远端实现的action名称,默认为函数名称
    - default_fn: 默认值函数,当远端无可调用实现时调用
    - cache: 缓存类型,默认为None,不缓存
    - cache_key_func: 缓存key生成函数,默认为hashkey
    - lock: 是否加锁,默认为False
    - timeout: 远端调用超时时间,默认为None,不超时
    """
    fn = args[0] if args.__len__() > 0 and inspect.isfunction(args[0]) else None
    if fn is None:
        return partial(
            remote_imp,
            action_key=action_key,
            default_fn=default_fn,
            cache=cache,
            lock=lock,
            cache_key_func=cache_key_func,
            timeout=timeout,
        ) # type: ignore
    
    return cast(RemoteImpAction[P, R], register_remote_imp_action(
        fn,
        action_key=action_key,
        default_fn=default_fn,
        cache=cache,
        lock=lock,
        cache_key_func=cache_key_func,
        timeout=timeout,
    ))

# @remote_imp(default_fn=lambda a,b:99)
# def test_remote_imp(a: int, b: int) -> str:...

# aa = test_remote_imp(1,2)

# register_remote_imp_action(test_remote_imp, "test_remote_imp2", default_fn=lambda a,b:3)