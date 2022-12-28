x = [4, 10, True, 'Hello']

print(x)
print(len(x))
x.append('World')
print(x)
print(len(x))

x.extend([12, 23, 1, 1, 2, 3, 4])
print(x)
print(len(x))

print(x.pop())
print(x.pop(1))
print(x)
y = ("Tuple", "Me", 123, True)
