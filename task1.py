import inspect

def strict(func):
    spec = inspect.getfullargspec(func)
    print(spec)
    def wrapper(*args, **kwargs):
        for i in range(len(args)):
            print("i = ", i, "name = ", spec.args[i],
                  "type = ", spec.annotations[spec.args[i]])
            if (type(args[i]) != spec.annotations[spec.args[i]]):
                raise TypeError
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
"""print(sum_two(1, 2.4))  # >>> TypeError"""


@strict
def fun(a: bool, b: int, c: float, d:str) -> int:
    return 1

print(fun(False, 1, 1.1, "1")) # >>> 1
print(fun(False, 1, 1.1, 1)) # >>> TypeError
