from ovld.types import Dataclass


class metatron(type):
    def __subclasscheck__(cls, c):
        return True

    # def __instancecheck__(cls, arg):
    #     print(cls)
    #     return arg == 3


class A(metaclass=metatron):
    pass


class B:
    pass


class C:
    pass


print(issubclass(B, A))
print(isinstance(B(), A))
# print(isinstance(3, A))


def see(x):
    ichk = type(x).__instancecheck__
    print(id(ichk), ichk)


see(Dataclass)
see(A)
see(C)
see(object)
see(int)
