class ClassB:
    @staticmethod
    def doBMethod():
        print('do A method()')

    def subtract(self, a, b):
        result = a - b
        return result


class BB:
    def __init__(self):
        self= self
        self.__private = 1
        self.public=2

    def sayHi(self):
        print('AA say hi: % %', self.__private, self.public)
       
    def __private():
        print("for only BB")        

def main():
    bb = BB()    
    bb.sayHi()

    classB = ClassB()
    if classB is not None:
        calcResult = classB.subtract(2,1)
        print(calcResult)
        
    ClassB.doBMethod()
    

main()    