import random

from warnings import warn
from typing import Iterable, Union, Type, NoReturn


def _election(__PIGS__):
    """
    this method will perform an election after each revolution.

    *note:*
    as this is a communist module, the election is protected
    and only __PIGS__ have access to it.
    """

    party = random.choices(__PIGS__, k=min(10, len(__PIGS__)))
    leader = random.choice(party)
    party.remove(leader)
    print(
        "Glorious election has been held with huge amount of participation (99.3%).",
        "\nSecretary General of the Party:",
        leader,
        "\nPeople's representatives:",
        party,
    )


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
            
    _election(__PythonIntrinsicGlobalStructures__)


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