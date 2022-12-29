def func():
    print('Run')


func()


def potato_generator(x):
    for i in range(x):
        print('Potato')

    return "potato", f"{x} potato"


r1, r2 = potato_generator(20)

print(r1, r2)
