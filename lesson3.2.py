my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) > 1:
    result = [my_list[-1]] + my_list[:-1]
else:
    result = my_list

print(result)

my_list = [1]
if len(my_list) > 1:
     result = [my_list[-1]] + my_list[:-1]
else:
    result = my_list

print(result)

my_list = [0]
if len(my_list) > 1:
    result = [my_list[-1]] + my_list[:-1]
else:
    result = my_list

print(result)

my_list = [1, 2, 3, 4, 5, 6, 7]
if len(my_list) > 1:
    result = [my_list[-1]] + my_list[:-1]
else:
    result = my_list
print(result)





















# [1] => [1]
# my_list = [1]
# len(my_list) <= 1
# result = my_list = [1]

# [0] => [0]
# my_list = []
# len(my_list) <= 1
# result = my_list = []


