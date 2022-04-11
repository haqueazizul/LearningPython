grocery_list = ['Egg', 'Rice', 'Milk', 'sugar']
grocery_list[2] = 'oil'
print(grocery_list[:2])
print(grocery_list[1:3])


price = [2, 4, 5, 10, 6, 7, 9]
max = price[0]
for value in price:
    if value > max:
        max = value

print(max)