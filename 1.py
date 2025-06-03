list = ["Филипп", "Степан", "Анна", "Влад", "Данил", "Алиса", "Денис", "Егор", "Артём", "Кира"]
names_starts_with_a = [string for string in list if string.startswith("А")]
print("Имена, начинающиеся на А: ", names_starts_with_a)