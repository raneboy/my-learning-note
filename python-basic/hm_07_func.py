import hm_07_func2 as multi


def a(x, y):
    result = x + y
    print(result)

def b(x, y=1):
    x += y
    print(x)


a(12, 13)
multi.multiply(12, 13)
b(12)

