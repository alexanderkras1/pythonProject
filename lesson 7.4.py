
def common_elements():
    lst_3 = set(range(0, 100, 3))
    lst_5 = set(range(0, 100, 5))

    return lst_3 & lst_5



print(common_elements())




# == {0, 75, 45, 15, 90, 60, 30}