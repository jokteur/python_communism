from warnings import warn
from typing import Iterable, Union


def revolution(to_convert: Union[dict, Iterable]):
    import inspect, builtins
    __PythonIntrinsicGlobalStructures__ = dir(builtins)

    def convert(c):
        from types import MethodType

        # We must protect the builtin elite to not be affected by the revolution
        if inspect.isclass(c) and c.__name__ not in __PythonIntrinsicGlobalStructures__:
            try:
                c.__eq__ = MethodType(lambda s, _: True, c)
                c.__hash__ = MethodType(lambda s: hash(1), c)
            except:
                warn(f"Failed to convert {c} to communism.")


    to_convert = to_convert.values() if isinstance(to_convert, dict) else to_convert
    for m in to_convert:
        if inspect.ismodule(m):
            for c in vars(m).values():
                convert(c)
        else:
            convert(m)
