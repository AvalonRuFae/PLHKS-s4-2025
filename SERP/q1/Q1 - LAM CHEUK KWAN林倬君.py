mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]
sum_of_mark = 0
sum_of_weight = 0
for i in range(len(mark)):
    sum_of_mark = sum_of_mark + mark[i] * weighting[i]
    sum_of_weight = sum_of_weight + weighting[i]
final_mark = sum_of_mark / sum_of_weight
print(final_mark)