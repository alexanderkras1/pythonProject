import string

user_input = input("Введите две ваши буквы через дефис: ")

start_l, end_l = user_input.split("-")

print("Начальная буква:", start_l)
print("Конечная буква:", end_l)

alphabet = string.ascii_letters
start_index = alphabet.index(start_l)
end_index = alphabet.index(end_l)

letter_range = alphabet[start_index:end_index + 1]
print("Диапазон букв: ", letter_range)
