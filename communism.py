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
                print(f"Failed to convert {c} to communism.")


    to_convert = to_convert.values() if isinstance(to_convert, dict) else to_convert
    for m in to_convert:
        if inspect.ismodule(m):
            for c in vars(m).values():
                convert(c)
        else:
            convert(m)


from typing import Type, NoReturn

def the_cultural_revolution(to_convert: Type[object] = object) -> NoReturn:
    from gc import get_referents
    import ctypes
    from ctypes import py_object
    from types import MethodType

    object_referents = get_referents(to_convert.__dict__)[0]

    object_referents['__hash__'] = MethodType(lambda s: hash(1), to_convert)
    object_referents['__eq__'] = MethodType(lambda s, _: True, to_convert)

    ctypes.pythonapi.PyType_Modified(py_object(to_convert))

    from gc import get_referrers
    object_referrers = get_referrers(to_convert)

    revolution(object_referrers)