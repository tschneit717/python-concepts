x = tuple(x for x in range(6))

print(x)

y = [[0 for x in range(10)] for x in range(5)]
print(y)

z = [i for i in range(100) if i % 12 == 0]
print(z)
print(type(z))
