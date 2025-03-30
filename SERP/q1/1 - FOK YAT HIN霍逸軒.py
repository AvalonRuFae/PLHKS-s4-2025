# Initialize marks and weightings
# mark = [75, 90, 60, 85, 80]  # This line is commented out
mark = [90, 80, 70, 75, 80]
weighting = [1, 1, 2, 2, 4]

# Initialize variable to store the weighted sum of marks
final_mark = 0

# Loop through each mark and weighting to calculate the weighted sum
for i in range(0, len(mark)):
    final_mark = final_mark + mark[i] * weighting[i]

# Initialize variable to store the sum of weights
sum_of_weight = 0

# Loop through each weighting to calculate the total weight
for i in range(0, len(weighting)):
    sum_of_weight = sum_of_weight + weighting[i]

# Calculate the final weighted average
final_mark = final_mark / sum_of_weight

# Print the final weighted average
print(final_mark)

# No logical issues found in this implementation.