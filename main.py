import random
from datetime import datetime


date = datetime.now()
print(date)
while True:
    listc = list()
    listb = list()
    count = 0
    balls = 0
    while True:
        firstc = random.randrange(1, 7)
        count += 1
        listc.append(firstc)
        if count == 1000:
            break

    if 1 in listc or 5 in listc:
        for i in listc:
            if i == 1:
                balls = balls + 10
            elif i == 5:
                balls = balls + 5
            else:
                continue
    print(balls)
    if balls < 2000 or balls == 2600:
        print(listc)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        for i in listc:
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
        break
    else:
        continue


date2 = datetime.now()
date3 = date2 - date
print(f"We need {date3} to get minimal balls")
print(f"Time when calculating ends is {date2}")
print(balls)
print(
    f'in range balls there are: ones - {count1}, twos - {count2}, threes - {count3}, fours - {count4}, fives - {count5}, sixs - {count6}')
# print(listb)
