# my_list = [0, 1, 0, 2, 3]
#
# el_1 = my_list.pop(2)
# el_2 = my_list.pop(0)
# my_list.insert(4 , el_1)
# my_list.insert(4 , el_2)
#
# print(my_list)

my_list = [0, 1, 0, 12, 3]
el = my_list.count(0)
without_0 = [ num for num in my_list if num != 0 ]
with_0 = [0] * el
res = without_0 + with_0

print(res)


my_list = [0]
el = my_list.count(0)
without_0 = [num for num in my_list if num != 0 ]
with_0 = [0] * el
res = without_0 + with_0

print(res)


my_list = [1, 0, 13, 0, 0, 0, 5]
el = my_list.count(0)
without_0 = [num for num in my_list if num != 0 ]
with_0 = [0] * el
res = without_0 + with_0

print(res)


my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
el = my_list.count(0)
without_0 = [num for num in my_list if num != 0 ]
with_0 = [0] * el
res = without_0 + with_0

print(res)

