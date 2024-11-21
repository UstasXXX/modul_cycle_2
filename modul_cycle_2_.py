my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list) :
    positiv_number = my_list[index]
    if positiv_number < 0:
        break
    if positiv_number > 0:
        print(positiv_number)
    index += 1
