# Initialize marks and weightings
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]

# Initialize variables to store the weighted sum of marks and the sum of weights
sum_of_mark = 0
sum_of_weight = 0

# Loop through each mark and weighting to calculate the weighted sum and total weight
for i in range(len(mark)):
    sum_of_mark = sum_of_mark + mark[i] * weighting[i]
    sum_of_weight = sum_of_weight + weighting[i]

# Calculate the final weighted average
final_mark = sum_of_mark / sum_of_weight

# Print the final weighted average
print(final_mark)

# No logical issues found in this implementation.