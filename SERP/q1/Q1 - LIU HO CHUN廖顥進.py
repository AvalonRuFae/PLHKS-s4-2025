mark=[90,80,70,75,80]
weighting=[1,1,2,2,4]
final_mark=0
sum_of_weight=0
for k in range(0,len(mark)):
    final_mark=final_mark+(mark[k]*weighting[k])
    sum_of_weight=sum_of_weight+weighting[k]
final_mark=final_mark/sum_of_weight


