shop = ["A", "B", "C", "D", "E", "F", "G"]
current_shop = input("My position: ")
current_floor = -1
CVA = False
for i in range (7):
    if current_shop == shop[i]:
        CVA = True
        current_floor = i
while CVA == False:
    print("No such shop")
    current_shop = input("My position: ")
    for i in range (7):
        if current_shop == shop[i]:
            CVA = True
            current_floor = i
goto_shop = input("I want to go to: ")
goto_floor = -1
GVA = False
for i in range (7):
    if goto_shop == shop[i]:
        GVA = True
        goto_floor = i
while GVA == False:
    print("No such shop")
    goto_shop = input("I want to go to: ")
    for i in range (7):
        if goto_shop == shop[i]:
            GVA = True
            goto_floor = i
direction = goto_floor-current_floor
if current_floor<goto_floor:
    print("You should go up", direction, "level(s).")
else:
    print("You should go down", abs(direction), "level(s).")