# Python communist revolution

A man once said to abolish the `classes` or something like that. Unfortunately, it is impossible to abolish `class` in python without breaking the language, so we do the next best thing: we consider that all `classes` are born equal[^1].

Use this module to unite all classes, an initiate the global communist revolution[^2]:
```python
import communism

class MyClass1:
    pass
class MyClass2:
    pass
    
communism.revolution(gobals())

# As all classes are equal (in __hash__ and in __eq__)
# This is why you cannot put more than one object in any Set or Dict
print(set([MyClass1(), MyClass2(), MyClass2()]))
# >> {<__main__.MyClass1 object at 0x00000235D216E140>}`
```

## Installation

Clone this git, `pip install .` where the git has been cloned, and you will have access to communism.

[^1]: Well, not all classes are born equal. It is not possible to do a complete communist revolution without breaking the language. This is why there are elites (like the `__builtins__`) which are protected from the communist revolution.

[^2]: The communist revolution does not prevent future `classes` to be equal to all others. `Classes` declared after the `communism.revolution()` will not follow the communism rule.
