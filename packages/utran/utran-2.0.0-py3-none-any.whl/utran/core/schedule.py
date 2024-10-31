import asyncio
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Tuple
from weakref import WeakSet
from functools import partial

from utran.core.backend.base import AbstractConnection
from utran.core.remote.action import RemoteImpAction, get_remote_imp_action
from utran.core.remote import worker as WorkerModule
from utran.log import logger
from utran.core.general import event_protocol
from utran.core.general.event_protocol import EventProtocolTypes
from utran.core.local import action as LocalActionModule
from utran.core import context

class ExecuteLocalActionError(Exception):
    """ 执行本地Action错误"""
    pass

class _WorkerDispatcher:
    """后端线程执行调度WorkerHandler"""

    already_imp_action: WeakSet[RemoteImpAction] = WeakSet()

    @classmethod
    def on_new_connection(cls, conn: AbstractConnection):
        imp_action_keys = conn.imp_ations
        actions = (get_remote_imp_action(k) for k in imp_action_keys)
        cls.already_imp_action.update(filter(None, actions))

    @classmethod
    def on_close_connection(
        cls,
        surplus_connections: Tuple[AbstractConnection, ...],
        cur_imp_action_keys: Tuple[str, ...],
    ):
        surplus_imp_action_keys = set(
            action for conn in surplus_connections for action in conn.imp_ations
        )
        imp_action_keys = [i for i in surplus_imp_action_keys if i not in cur_imp_action_keys]
        actions = (get_remote_imp_action(k) for k in imp_action_keys)
        cls.already_imp_action.difference_update(filter(None, actions))
        

    @classmethod
    def dispatch_worker(cls, pool: ThreadPoolExecutor):
        class_worker_handlers = [
            worker_handler
            for worker_handler in WorkerModule._Store._STORE_WORKER_OF_CLASS.values()
            if worker_handler.use_remote_actions.issubset(cls.already_imp_action)
            and not worker_handler.is_runing
            and not worker_handler.is_completed
            and not worker_handler.is_abandoned
        ]
        func_worker_handlers = [
            worker_handler
            for worker_handler in WorkerModule._Store._STORE_WORKER_OF_FUNC.values()
            if worker_handler.use_remote_actions.issubset(cls.already_imp_action)
            and not worker_handler.is_runing
            and not worker_handler.is_completed
            and not worker_handler.is_abandoned
        ]

        all_run_worker = class_worker_handlers + func_worker_handlers
        if not all_run_worker:
            return

        # 使用线程池执行
        for worker_handler in all_run_worker:
            pool.submit(worker_handler).add_done_callback(
                partial(cls.__on_worker_done, worker_handler)
            )

        logger.debug(f"{len(all_run_worker)} workers dispatched.")

    @classmethod
    def __on_worker_done(cls, worker_handler: WorkerModule._WorkerHandler, fut: Future):
        try:
            fut.result()
        except Exception as e:
            raise RuntimeError(f"worker internal error: {e}") from e
        finally:
            worker_handler.is_runing = False


class LocalActionDispatcher:
    """后端线程执行调度本地Action"""

    @classmethod
    def call_local(
        cls,
        pool: ThreadPoolExecutor,
        action: LocalActionModule.LocalAction,
        params: dict,
        future: asyncio.Future,
    ):
        """本地同步Action调用"""
        logger.debug(f"执行本地action调用: {action}")
        _args = params.get("args", [])
        _kwargs = params.get("kwargs", {})
        
        # 打印线程池剩余数量
        logger.info(f"thread pool size: {pool._max_workers - pool._work_queue.qsize()}")
        
        if action.is_async():
            # 使用主事件循环，执行异步本地调用 
            asyncio.run_coroutine_threadsafe(action(*_args, **_kwargs), future.get_loop()).add_done_callback(
                partial(cls.__on_local_action_done, future)
            )
        else:
            # 使用线程池，执行同步本地调用
            pool.submit(action, *_args, **_kwargs).add_done_callback(
                partial(cls.__on_local_action_done, future)
            )


    @classmethod
    def __on_local_action_done(cls, future: asyncio.Future, exe_fut: Future):
        """本地Action调用完成"""
        
        if future.done(): return   # 当futrue完成时，说明被撤销，直接返回
        try:
            result = exe_fut.result()
            future.get_loop().call_soon_threadsafe(future.set_result, result)
        except Exception as e:
            err = ExecuteLocalActionError(f"执行本地Action错误: {e}")
            future.get_loop().call_soon_threadsafe(future.set_exception, err)
            raise err from e



class Dispatcher:
    """总调度器"""

    __slots__ = ()


    @property
    def queue(self):
        return context.__UTRAN_CONTEXT__["backend_queue"]

    @property
    def pool(self):
        return context.__UTRAN_CONTEXT__["worker_pool"]

    @property
    def loop(self):
        return context.__UTRAN_CONTEXT__["backend_loop"]

    def _do_event_new_connection(self, event: event_protocol.NewConnectionEvent):
        # 由后端线程队列触发
        _WorkerDispatcher.on_new_connection(event["conn"])
        _WorkerDispatcher.dispatch_worker(self.pool)

    def _do_event_close_connection(
        self,
        event: event_protocol.CloseConnectionEvent,
    ):
        # 由后端线程队列触发
        _WorkerDispatcher.on_close_connection(
            surplus_connections=event["surplus_connections"],
            cur_imp_action_keys=event["cur_imp_action_keys"],
        )

    def _do_event_executor_worker(self):
        # 由后端线程队列触发
        _WorkerDispatcher.dispatch_worker(self.pool)

    def _do_event_execute_local_action(
        self,
        event: event_protocol.ExecuteLocalActionEvent,
    ):
        # 由后端线程队列触发
        LocalActionDispatcher.call_local(
            pool=self.pool,
            action=event["action"],
            params=event["params"],
            future=event["future"],
        )


    def invoke_local_action(
        self,
        action: LocalActionModule.LocalAction,
        params: dict,
    ):
        """执行本地Action"""
        # if action.is_async():
        #     _args = params.get("args", [])
        #     _kwargs = params.get("kwargs", {})
        #     return action(*_args, **_kwargs)

        fu = asyncio.get_running_loop().create_future()
        event: event_protocol.ExecuteLocalActionEvent = {
            "type": EventProtocolTypes.execute_local_action,
            "action": action,
            "params": params,
            "future": fu,
        }
        self.loop.call_soon_threadsafe(self.queue.put_nowait, event)
        return fu


    def invoke_executor_worker(self):
        """执行调度WorkerHandler"""
        # 使用线程安全加入队列
        event: event_protocol.ExecuteWorkerEvent = {
            "type": EventProtocolTypes.execute_worker,
        }
        self.loop.call_soon_threadsafe(self.queue.put_nowait, event)

    def invoke_new_connection(self, conn: AbstractConnection):
        # 使用线程安全加入队列
        event: event_protocol.NewConnectionEvent = {
            "type": EventProtocolTypes.new_connection,
            "conn": conn,
        }
        self.loop.call_soon_threadsafe(self.queue.put_nowait, event)

    def invoke_close_connection(
        self,
        surplus_connections: tuple[AbstractConnection, ...],
        /,
        *cur_imp_action_keys: str,
    ):
        # 使用线程安全加入队列
        event: event_protocol.CloseConnectionEvent = {
            "type": EventProtocolTypes.close_connection,
            "surplus_connections": surplus_connections,
            "cur_imp_action_keys": cur_imp_action_keys,
        }
        self.loop.call_soon_threadsafe(self.queue.put_nowait, event)




async def run_backend_queue_forever():

    dispatcher = context.__UTRAN_CONTEXT__["host_instance"].dispatcher
    event_handlers = {
        EventProtocolTypes.new_connection: dispatcher._do_event_new_connection,
        EventProtocolTypes.close_connection: dispatcher._do_event_close_connection,
        EventProtocolTypes.execute_worker: dispatcher._do_event_executor_worker,
        EventProtocolTypes.execute_local_action: dispatcher._do_event_execute_local_action
    }
    
    while True:
        queue = context.__UTRAN_CONTEXT__["backend_queue"]
        try:
            event = await queue.get()
            logger.debug(f"received dispatcher event: {event}")

            if event_type := event["type"]:
                handler = event_handlers.get(event_type)
                if handler:
                    handler(event)
                else:
                    logger.error(f"unknown event: {event}")
        except Exception as e:
            logger.error(f"backend queue error: {e}")
        finally:
            queue.task_done()
