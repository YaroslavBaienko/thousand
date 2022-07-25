def countDices(numbers, list1):
    print(list1)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for i in list1:
        if i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1
        elif i == 3:
            count3 += 1
        elif i == 4:
            count4 += 1
        elif i == 5:
            count5 += 1
        else:
            count6 += 1
    return f'in range balls there are: ones - {count1}, twos - {count2}, threes - {count3}, fours - {count4}, fives - {count5}, sixs - {count6}'
