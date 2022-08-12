from typing import Callable


class Factory:
    def __init__(self) -> None:
        self.func_table = dict()

    def register(self, *name: str):
        def wrapper(func):
            for key in name:
                if key in self.func_table:
                    raise Exception(f"{key} already registers")
                self.func_table[key] = func
            return func
        return wrapper

    def get_func(self, name: str) -> Callable:
        if name not in self.func_table:
            raise Exception(f"{name} not in func table")
        return self.func_table[name]


_factory = Factory()


def get_factory():
    return _factory