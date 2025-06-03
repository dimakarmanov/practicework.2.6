list = [-7, 3, -10, 2, 1, -8, 8, -5, -3, 0]
first_positive = None
last_negative = None

for num in list:
    if num > 0 and first_positive is None:
        first_positive = num

    if num < 0:
        last_negative = num

print("Первый положительный и последний отрицательный: ", first_positive,last_negative)