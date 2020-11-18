# # 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def odd_item(a):
#     # return_list = []
#     # for i in range(len(a)):
#     #     if i % 2 == 1:
#     #         return_list.append(a[i])
#     # return return_list
#     return a[1::2]
#
# print(odd_item((1, 2, 3, 4, 5, 6, 7)))



# # 3..写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def gt5(a):
#     if len(a) > 5:
#         return True
#     else:
#         return False
#     # return True if len(a) > 5 else False
#
# print(gt5('ebf'))


# # 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def first_two(a):
#     return a[:2] if len(a) > 2 else a
#
# print(first_two([1, 2, 3, 4, 5]))
# print(first_two([1]))



# # 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
# def digit_alpha_other(s):
#     digit = 0
#     alpha = 0
#     other = 0
#     for i in s:
#         if i.isdigit():
#             digit += 1
#         elif i.isalpha():
#             alpha += 1
#         else:
#             other += 1
#     return digit, alpha, other
#
# print(digit_alpha_other('xjsh293hfdn3i-2932;'))


# # 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def greater_one(a, b):
#     return a if a > b else b
#
# print(greater_one(1, 2))



# # 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。 dic = {"k1": "v1v1", "k2": [11,22,33,44]} PS:字典中的value只能是字符串或列表
# def keep_first_two(dic):
#     for k, v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic
#
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(keep_first_two(dic))



# # 8.写函数，此函数只接收一个参数这个参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def index_item(a_list):
#     dic = {}
#     for i in enumerate(a_list):
#         dic[i[0]] = i[1]
#     return dic
#
# print(index_item([2, 5, 6, 8, 9]))


# # 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def write_to_file(name, gender, age, education):
#     info = 'name: {}, gender: {}, age: {:.2f}, education: {}\n'.format(name, gender, age, education)
#     with open('hw09_student_msg', mode='a', encoding='utf-8') as f1:
#         f1.write(info)
#
#
# name = input('name: ')
# gender = input('gender: ')
# age = float(input('age: '))
# education = input('education: ')
#
# write_to_file(name, gender, age, education)


# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
def write_to_file(name, age, education, gender='male'):
    info = 'name: {}, gender: {}, age: {}, education: {}\n'.format(name, gender, age, education)
    with open('hw09_student_msg', mode='a', encoding='utf-8') as f1:
        f1.write(info)

while True:
    name = input('name: ')
    if name.upper() == 'Q':
        break
    gender = input('gender: ')
    if gender.upper() == 'Q':
        break
    age = input('age: ')
    if age.upper() == 'Q':
        break
    education = input('education: ')
    if education.upper() == 'Q':
        break
    if gender == 'female':
        write_to_file(name, age, education, gender)
    else:
        write_to_file(name, age, education)





