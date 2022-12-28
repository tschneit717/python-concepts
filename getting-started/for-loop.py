for i in range(1, 10, 3):
    print(i)

# start, stop, step
# stop = default
x = [4, 21, 123, 123123, 555]

for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element)
