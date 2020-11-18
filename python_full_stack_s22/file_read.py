f = open("小重山", 'r', encoding='utf8')

print(f.read())

# f为迭代器
for i in f:
    print(i.strip())


f.close()