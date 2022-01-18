import communism
from communist import Communist


class MyClass1(Communist):
    pass


class MyClass2:
    pass


communism.revolution(globals())

# As all classes are equal (in __hash__ and in __eq__)
# This is why you cannot put more than one object in any Set or Dict
print(set([MyClass1(), MyClass2(), MyClass2()]))