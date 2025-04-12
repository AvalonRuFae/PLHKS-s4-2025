the_list = [12, 8, 40, 23, 6]
if the_list[0] > the_list[1]:
    maximum=the_list[0]
    secondmax=the_list[1]
else:
    maximum=the_list[1]
    secondmax=the_list[0]
for i in range(2,5):
    if the_list[i] > maximum:
       secondmax= maximum
       maximum=the_list[i]
    elif the_list[i] > secondmax:
        secondmax=the_list[i]

