def is_even(digit):
    if digit % 2 == 0:
        print("Число четное")
        return True
    else:
        print("Число нечетное")
        return False


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

