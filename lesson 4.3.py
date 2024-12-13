import random

my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(my_list)


lst1 = [my_list[0]]
lst2 = [my_list[2]]
lst3 = [my_list[-2]]

new_list = lst1 + lst2 + lst3


print(new_list)


