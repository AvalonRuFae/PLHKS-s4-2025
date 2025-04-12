list = [12, 8, 40, 23, 6]
if list[0] > list[1]:
    maximum = list[0]
    secondmax = list[1]
else:
    maximum = list[1]
    secondmax = list[0]

for i in range (2,5):
    if list[i] > maximum:
        secondmax = maximum
        maximum = list[i]
    elif list[i] > secondmax:
        secondmax = list[i]
print(secondmax)