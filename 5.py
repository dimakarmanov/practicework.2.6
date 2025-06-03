C = "б"
A = ["банан", "яблоко", "берёза", "баобаб", "коромысло", "б"]
count = 0
for string in A:
    if len(string) > 1:
        if string.startswith(C) and string.endswith(C):
            count += 1
print("Кол-тво элементов A, начинающихся и заканчивающихся на C: ", count)