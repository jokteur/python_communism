from communist import Communist

global gloriousLeader


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GloriousLeader(metaclass=Singleton):
    def elect(self, new_leader):
        self = new_leader

    def __eq__(self, other):
        return False

    def __hash__(self):
        return hash(2)

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False


gloriousLeader = GloriousLeader()
