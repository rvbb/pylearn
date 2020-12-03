class Parent:
    def override_method(self):
        print('parent "Override" method')

    def overload_method(self):
        print('parent method')


class Child(Parent):
    def fn(self, a):
        print("this is a=", a)
