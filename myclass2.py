from interface import MyClass


class MyClass2(MyClass):
    def aa(self) -> any:
        pass

    def _texst(self):
        print("hello")

a=MyClass2()
a._texst()