# Initialize the price list for each set (index 0 corresponds to set 1, and so on)
price = [39.9, 34.9, 45.9, 40, 79.9]

# Prompt the user to input their order (1-5) or -1 to stop
order = int(input("What is your order (1-5): "))

# Initialize the checkout total to 0
checkout = 0

# Loop until the user enters -1
while order != -1:
    # Check if the order is valid (between 1 and 5 inclusive)
    if order > 0 and order < 6:
        # Add the price of the selected set to the checkout total
        checkout = checkout + price[order-1]  # Fixed logical issue: Use order-1 to access the correct index
    else:
        # Print an error message for invalid input
        print("Invalid")
    # Prompt the user for the next order
    order = int(input("What is your order (1-5): "))

# Print the total checkout amount
print("Checkout:", checkout)

# No logical issues found in this implementation.