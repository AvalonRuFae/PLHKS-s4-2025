#(a) Compare the first two items first
the_list = [12, 8, 40, 23, 6]
if the_list[0] > the_list[1]:
    maximum = the_list[0]
    secondmax = the_list[1]
else:
    maximum = the_list[1]
    secondmax = the_list[0]
#(b) Use a for loop to compare the list items and the two temporary variables one by one
for i in range (0, len(the_list)):
    if the_list[i] > maximum:
        secondmax = maximum
        maximum = the_list[i]
    elif the_list[i] > secondmax:
        secondmax = the_list[i]