import communism


class MyClass1:
    pass


class MyClass2:
    pass


communism.revolution(globals())

# As all classes are equal (in __hash__ and in __eq__)
# This is why you cannot put more than one object in any Set or Dict
print({MyClass1(), MyClass2(), MyClass2()})

print('\n\nNew classes are born after the first revolution.')
class RisingElites:
    pass

class Oligarchs:
    pass

print({RisingElites(), Oligarchs(), Oligarchs()})

print('\n\nStart the cultural revolution...')

communism.the_cultural_revolution(object)

print({RisingElites(), Oligarchs(), Oligarchs()})

print('\n\nAgain new classes are born after the cultural revolution.')

class BusinessMen:
    pass

class Intellectuals:
    pass

print({BusinessMen(), BusinessMen(), RisingElites(),
       Oligarchs(), Oligarchs(), Intellectuals(),
        MyClass1(), MyClass1(), MyClass2(), MyClass2(),
       })