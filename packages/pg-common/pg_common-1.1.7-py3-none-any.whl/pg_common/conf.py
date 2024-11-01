__all__ = ["RuntimeException", "GLOBAL_DEBUG", "GameErrorCode", "GameException"]
__auth__ = "baozilaji@gmail.com"


GLOBAL_DEBUG = False


class GameErrorCode(object):
    RECEIVE_INPUT_ERROR = -100000
    NO_MATCHED_METHOD_ERROR = -100001
    OTHER_EXCEPTION = -100002

class RuntimeException(Exception):
    """
      全局运行时异常
    """
    def __init__(self, name: str, msg: str):
        self.name = name
        self.msg = msg


class GameException(Exception):

    def __init__(self, state: int, msg: str):
        self.state = state
        self.msg = msg

    def __str__(self):
        return f"\"{self.state}, {self.msg}\""

    def __repr__(self):
        return self.__str__()
