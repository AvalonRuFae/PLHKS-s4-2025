#mark = [75, 90, 60, 85, 80]
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]
final_mark = 0
for i in range(0,len(mark)):
    final_mark = final_mark + mark[i]*weighting[i]
sum_of_weight = 0
for i in range(0,len(weighting)):
    sum_of_weight = sum_of_weight + weighting[i]
final_mark = final_mark/sum_of_weight
print(final_mark)