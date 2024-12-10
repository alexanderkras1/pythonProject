my_list = []

if len(my_list) == 0:
    result = [[], []]

else:
    x = (len(my_list) + 1) // 2

    part1 = my_list[:x]
    part2 = my_list[x:]
    result = [part1, part2]

print(result)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] => [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11]]
# [1, 2, 3, 4, 5, 6, 7, 8] => [[1, 2, 3, 4], [5, 6, 7, 8]]
# [1] => [[1], []]
# [] => [[], []]



