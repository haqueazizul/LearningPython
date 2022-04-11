number_list = [1, 2, 3, 4, 5, 6, 5, 2, 8, 9, 22]
unique = []
for number in number_list:
    if number not in unique:
        unique.append(number)
print(unique)