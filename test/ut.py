import sys
# sys.path.append('Z:/code/mine/pylearn/demo')
# sys.path.insert(1, 'Z:/code/mine/pylearn/demo')
sys.path.append("./demo")
import pkgb as b
import pkga.obj1 as a1
# import pkga.obj2 as a2 # --> make Error ModuleNotFoundError: No module named 'obj1' in obj2.py


def main():
    b1 = b.Demo()
    b1.abc()

    print("multi is ", a1.multi(2,3))

    # object2 = a2.Ob2()
    # print(object2.add(2,3))

main()    