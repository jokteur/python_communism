import random
from typing import Iterable, Union
from warnings import warn

from communist import Communist
from glorious_leader import GloriousLeader

gloriousLeader = GloriousLeader()


def _election(__PIGS__):
    global gloriousLeader
    """
    this method will perform an election after each revolution.

    *note:*
    as this is a communist module, the election is protected
    and only __PIGS__ have access to it.
    """

    party = random.choices(__PIGS__, k=min(10, len(__PIGS__)))
    elected = random.choice(party)
    gloriousLeader.elect(elected)
    party.remove(elected)
    print(
        "Glorious election has been held with huge amount of participation (99.3%).",
        "\nSecretary General of the Party:",
        gloriousLeader.leader,
        "\nPeople's representatives:",
        party,
    )


def revolution(to_convert: Union[dict, Iterable]):
    import inspect, builtins

    __PythonIntrinsicGlobalStructures__ = dir(builtins)

    def convert(c):
        from types import MethodType

        # We must protect the builtin elite to not be affected by the revolution
        if inspect.isclass(c) and is_not_elite(c) and is_not_comrade(c):
            try:
                c.__eq__ = MethodType(lambda s, _: True, c)
                c.__hash__ = MethodType(lambda s: hash(1), c)
            except:
                warn(f"Failed to convert {c} to communism.")

    def is_not_elite(c):
        return c.__name__ not in __PythonIntrinsicGlobalStructures__

    def is_not_comrade(c):
        return type(c) is not Communist

    to_convert = to_convert.values() if isinstance(to_convert, dict) else to_convert
    for m in to_convert:
        if inspect.ismodule(m):
            for c in vars(m).values():
                convert(c)
        else:
            convert(m)

    _election(__PythonIntrinsicGlobalStructures__)
