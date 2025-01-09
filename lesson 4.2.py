my_list = [0, 1, 7, 2, 4, 8]
first_list = my_list[::2]
sum_l = first_list[0] + first_list[1] + first_list[2]
res = sum_l * my_list[-1]

print(res)


my_list = [1, 3, 5]
first_list = my_list[::2]
sum_l = first_list[0] + first_list[1]
res = sum_l * my_list[-1]

print(res)

my_list = [6]
first_list = my_list[::2]
sum_l = first_list[0]
res = sum_l * my_list[-1]
print(res)


my_list =[]
first_list = my_list[::2]
sum_l = first_list[0] + first_list[1] if len(first_list) > 1 else sum(first_list)
res = sum_l * my_list[-1] if my_list else 0
print(res)