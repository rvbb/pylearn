class ClassA:
    def doAMethod():
        print('do A method()')

    def multi(a, b):
        result = a + b
        return result

class AA:     
    def __init__(seft):
        seft.public = "Public variable"
        seft.__private = "private variable"
        seft._protected = "protected variable"

    def sayHi():
        print("AA say hi! ", seft.public)