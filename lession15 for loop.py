for character in 'Python':
    print(character)

for item in ['Egg', 'Rcie', 'Oil']:
    print(item)

for number in range(5, 10, 2):
    print(number)

bills = [10, 30, 40, 50, 20]
total = 0
for bill in bills:
    total = total + bill
print(f"Total bill: ${total}")