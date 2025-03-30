# Initialize marks and weightings
# mark = [75, 90, 60, 85, 80]  # This line is commented out
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]

# Initialize variables to store the weighted sum of marks and the sum of weights
final_mark = 0
sum_of_weight = 0

# Loop through each mark and weighting to calculate the weighted sum and total weight
for i in range(4):  # Logical issue: The range is hardcoded to 4, which may cause errors if the arrays are modified
    final_mark = final_mark + mark[i] * weighting[i]
    sum_of_weight = weighting[i] + sum_of_weight

# Calculate the final weighted average
overall_result = final_mark / sum_of_weight

# Print the final weighted average
print(overall_result)

# Logical issue: The code assumes the length of the arrays is always 4, which may cause errors if the arrays are modified. Also, the length of the array is already not four in this case already. range(4) refers to 0,1,2,3 and does not include 4, what you may want to do should be range(5). Of course, range(len(mark)) is a better choice.