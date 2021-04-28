class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError(x, " is not positive")


x = PositiveList()
print(x)
x.append(3)
print(x)
x.append(0)
print(x)
x.append(-1)
print(0)
