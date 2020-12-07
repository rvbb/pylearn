import sys
# sys.path.append('Z:/code/mine/pylearn/demo')
# sys.path.insert(1, 'Z:/code/mine/pylearn/demo')
sys.path.append("./demo")
import pkgb as b
import pkga.obj1 as a1
# import pkga.obj2 as a2 # --> make Error ModuleNotFoundError: No module named 'obj1' in obj2.py
import common as c

def main():
    b1 = b.Demo()
    b1.abc()

    print("multi is ", a1.multi(2,3))

    # object2 = a2.Ob2()
    # print(object2.add(2,3))
    c1 = c.Common()
    # del c1
    c1.json()
    c.Common().json_dump()

    #list
    l = c.List()
    l.make_alist()   
    l.remove_duplicate()

    #tuple
    t = c.Tuple()
    t.make()

    #set
    s = c.Set()
    s.make()

    #dict
    d = c.Dict()
    d.make()
    anyobject = c.AnyObject("A", "B")
    d.of(anyobject)

    #Operation
    o = c.Ops()
    s1 = o.make()
    print(s1)

    r1 = "abc"[::-1]
    print(r1)   

main()    