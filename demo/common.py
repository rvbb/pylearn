import json

class Parent:
    def override_method(self):
        print('parent "Override" method')

    def overload_method(self):
        print('parent method')


class Child(Parent):
    def fn(self, a):
        print("this is a=", a)


class Common:
    def json(self):
        x =  '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        print(y["age"])

    def json_dump(self):
        x = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        y = json.dumps(x)
        print(y)

#not ordered, allow duplicate, allow None
class List:
    def make_alist(self):
        alist = [1,2,3,"123",'one']
        alist[0] = "11"
        print("list=", alist)
        alist.append("two")
        print("after", alist)

        matrix = [[1,2], ['one', 'two']]
        print("matrix", matrix)

    def remove_duplicate(self):
        l = [1,1,2,2,3]
        s = set(l)
        print("result after remove dupplicated value in list", list(s))

# Orderd, unchangeble(Immutable) - not add, allow dupplicate
class Tuple:
    def make(self):
        t = (5,1,1,2,'', None)
        # is not tuple
        t1= ("one value")
        #t.append("2") -> raise error        
        print("is tuple=", type(t1))
        print("tuple", t)

# Orderd, unchangeble(Immutable), NOT allow dupplicate
class Set:
    def make(self):
        s = {5,1,2,'', None}
        s1 = set((1,2, 3.4))
        print("set={0}, {1}".format(s, s1))


# unOrderd, changeble, NOT allow dupplicate, allow one None key
class AnyObject:
    def __init__(self, a, b):
        self.aa = a
        self.bb = b

class Dict:
    def make(self):
        d = {"k1":5,"k2":"xxx", 1:2, "t":None, "t1":None, None: '123', 'None': '123'}
        print("dictionary=", d) 

    def of(self, any_object):
        print("aa={0}, b= {1}".format(any_object.aa, any_object.bb))

class Ops:
    def make(self) -> str:
        ao1 = AnyObject(1,2)
        ao2 = AnyObject(1,2)
        ao3 = ao2
        print("compare object={0}".format(ao1 is ao2))
        print("compare value={0}, {1}".format(ao1 == ao2, ao2 == ao3))
        try:
            s = str(ao3)
            del s
        except TypeError as exp:
            print('got exception')
            raise TypeError('Errrrrrrrrrrr = ', exp)
        
        return ao3

class Lambda:
    def make(self, x):
        b = lambda a: a*2*x
        return b(5)