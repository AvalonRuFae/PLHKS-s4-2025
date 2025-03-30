# Initialize marks and weightings
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]

# Initialize variables to store the weighted sum of marks and the sum of weights
final_mark = 0
sum_of_weight = 0

# Loop through each mark and weighting to calculate the weighted sum and total weight
for k in range(0, len(mark)):
    final_mark = final_mark + (mark[k] * weighting[k])
    sum_of_weight = sum_of_weight + weighting[k]

# Calculate the final weighted average
final_mark = final_mark / sum_of_weight

# No logical issues found in this implementation.


