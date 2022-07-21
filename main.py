from distutils.command.build_scripts import first_line_re
import random

listc = list()
listb = list()
count = 0
balls = 0

while True:
    firstc = random.randrange(1, 5)
    count += 1
    listc.append(firstc)
    if count == 5:
        break


print(listc)
if 1 in listc or 5 in listc:
    for i in listc:
        if i == 1:
            balls = balls + 10
        elif i == 5:
            balls = balls + 5
        else:
            continue

print(balls)
# print(listb)
