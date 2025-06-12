class SumAll:
    def __init__(self):
        self.__res = 0

    @property
    def result(self) -> int | float:
        return self.__res

    def __call__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)):
                self.__res += arg
            else:
                raise ValueError("Only numbers are allowed")

        return self


s = SumAll()
x = 2
y = "gsdfhjkhdfgjk"

def test(x):
    print(x)


print("x", callable(x))
print("y", callable(y))
print("s", callable(s))
print("test", callable(test))
