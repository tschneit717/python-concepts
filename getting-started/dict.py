x = {"key": 5}
x["key23"] = 555
print(x)
print('key' in x)
print(list(x.values()))

del x['key23']
print(x)

for key, value in x.items():
    print(key, value)
