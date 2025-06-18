import inspect

def strict(func):
    spec = inspect.getfullargspec(func)
    def wrapper(*args, **kwargs):
        for i in range(len(args)):
            if (type(args[i]) != spec.annotations[spec.args[i]]):
                raise TypeError
        return func(*args, **kwargs)
    return wrapper



@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def fun(a: bool, b: int, c: float, d:str) -> int:
    return 1


import unittest

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_two(1, 2), 3)
    def test_2(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)
    def test_3(self):
        self.assertEqual(fun(False, 1, 1.1, "1"), 1)
    def test_4(self):
        with self.assertRaises(TypeError):
            print(fun(False, 1, 1.1, 1))
    def test_4(self):
        with self.assertRaises(TypeError):
            print(fun(False, 1.0, 1.1, "1"))
    def test_4(self):
        with self.assertRaises(TypeError):
            print(fun(False, 1, 1.1, False))
    
    
if __name__ == '__main__':
    unittest.main()
