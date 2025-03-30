#mark = [75, 90, 60, 85, 80]
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]
final_mark = 0
sum_of_weight = 0
for i in range (4):
    final_mark=final_mark+mark[i]*weighting[i]
    sum_of_weight=weighting[i]+sum_of_weight
overall_result=final_mark/sum_of_weight
print(overall_result)