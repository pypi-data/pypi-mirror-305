class RemoteRunActionError(Exception):
    """远程调用错误"""

    # def __repr__(self) -> str:
    #     return f"{self.__class__.__name__} ({' '.join(self.args)})"

    # def __str__(self) -> str:
    #     return self.__repr__()

class RemoteResultError(RemoteRunActionError):
    """远程调用结果错误，即: 远程调用成功, 但是远程调用返回的结果中包含error字段"""

    ...


class RemoteRuntimeError(RemoteRunActionError):
    """远程调用运行时,发生内部错误"""

    ...


class RemoteTimeoutError(RemoteRunActionError):
    """远程调用超时错误"""

    ...


class RemoteNotImplementedError(RemoteRunActionError):
    """远程无可调用实现"""

    ...
