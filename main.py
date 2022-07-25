import random
from datetime import datetime
import funtions


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
    if balls < 3000 or balls == 2600:
        difnumbers = funtions.countDices(balls, listc)
        break
    else:
        continue


date2 = datetime.now()
date3 = date2 - date
print(f"We need {date3} to get minimal balls")
print(f"Time when calculating ends is {date2}")
print(balls)
print(difnumbers)
# print(listb)
