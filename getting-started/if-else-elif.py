name = input("Name: ")
age = input("Age: ")

if int(age) > 18:
    print('you are an adult')
elif int(age) < 10:
    print('what are you doing here')
else:
    print('You are not an adult')
