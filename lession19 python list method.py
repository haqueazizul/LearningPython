number_list = [1, 2, 3, 4, 5, 6, 7, 11, 23]
number_list.append(20)
number_list.insert(1,33)
number_list.remove(2)
number_list.sort()
number_list.reverse()

print(number_list)
print(1 in number_list)
print(number_list.count(1))
print(number_list.index(3))

number_list.pop()

number_list2 = number_list.copy()
number_list2.clear()
print(number_list2)