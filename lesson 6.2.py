total_seconds = int(input("Введите ваше число от 0 до 8640000: "))



days, remaining_seconds = divmod(total_seconds, 86400) # 86400 секунд в дне

hours, remaining_seconds = divmod(remaining_seconds, 3600) # 3600 секунд в часе

minutes, seconds = divmod(remaining_seconds, 60) # 60 секунд в минуте

print(f"{days} дней, {hours:02}:{minutes:02}:{seconds:02}")