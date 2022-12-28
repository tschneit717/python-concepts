x = set()
s = {1, 3, 9, 27, 1}
s2 = [1, 3, 9, 27, 1]
s.add(1000)

x.add('hello')
print("hello" in x)
print(4 in s)
print(x)
print(s)

print(x.union(s))
