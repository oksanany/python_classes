# title Print Hello World
# description Напечатать на экран hello, если число делится на 3; world, если число делаится на 5, и само число, иначе.
# ---end----

def helloWorld(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print('hello, world!')
        elif i % 3 == 0:
            print('hello', end = '')
        elif i % 5 == 0:
            print('world', end='')
        else:
            print(i)