# while 实现循环for的功能

s = 'abcdefg'

s1 = s.__iter__()
while True:
    try:
        print(s1.__next__())
    except StopIteration:
        break

