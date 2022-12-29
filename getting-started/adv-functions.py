def func(x):
    def func2():
        print(x)
    return func2


x = func(3)
print(func(3)())

x()


def func3(*args, **kwargs):
    print(*args)


x = [1, 23233, 12323123, 848483]
print(*x)

w = 10


def function(x, y):
    w = 'water'
    print(w)
    print(x, y)


print(w)

pairs = [(1, 2), (3, 4)]

for pair in pairs:
    function(*pair)
function(**{'x': 2, 'y': 5})

# kwargs = keyword args
func3(1, 2, 3, 4, 5, one=0, two=1)
