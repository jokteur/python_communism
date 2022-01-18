class Communist:
    def __eq__(self, other):
        if type(other) is Communist:
            return True
        return False

    def __hash__(self):
        return hash(True)

    def __gt__(self, other):
        if type(other) is Communist:
            return False
        super.__gt__(self, other)

    def __lt__(self, other):
        if type(other) is Communist:
            return False
        super.__gt__(self, other)
