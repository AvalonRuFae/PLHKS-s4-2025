shop = ["A", "B", "C", "D", "E", "F", "G"]
current_shop = input("My position: ")
current_floor = -1
#(a) To find the floor that the inputted shop is on
for i in range(len(shop)):
    if current_shop== shop[i]:
        current_floor=i
#(b) Asks the user to input again and reorientates itself
#    when it cannot find the shop inputted by the user
while current_floor == -1:
    print("No such shop")
    current_shop= input("My position:")
    for i in range(len(shop)):
        if current_shop== shop[i]:
           current_floor=i
#(c) To find the floor that the target shop is on
#    and check whether the user input is valid
goto_shop = input("I want to go to: ")
goto_floor = -1
for k in range(len(shop)):
    if goto_shop== shop[k]:
        goto_floor=k
while goto_floor==-1:
    print("No such shop")
    goto_shop= input("My position:")
    for k in range(len(shop)):
        if goto_shop== shop[k]:
           goto_floor=k
#(d) Calculate the distance between the two shops,
#    then determine the floor and direction that the user should go to
direction =goto_floor-current_floor
if direction >0:
    print("You should go up", direction, "level(s).")
else:
    print("You should go down", abs(direction), "level(s).")