from communist import Communist


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GloriousLeader(Communist, metaclass=Singleton):
    leader = None

    def __init__(self, leader = None):
        self.leader = leader

    def elect(self, newLeader):
        self.leader = newLeader

    def __eq__(self, other):
        return False

    def __hash__(self):
        return hash(2)

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False

