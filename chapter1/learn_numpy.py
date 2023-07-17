from numpy import *


def foo():
    a = mat(random.rand(2, 2))
    b = a.I
    print(a)
    print("=========")
    print(b)
    print("=========")
    print(a * b)


if __name__ == "__main__":
    foo()
