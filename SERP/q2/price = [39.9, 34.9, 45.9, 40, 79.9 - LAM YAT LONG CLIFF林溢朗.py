price = [39.9, 34.9, 45.9, 40, 79.9]
order = int(input("What is your order (1-5): "))
checkout = 0
while order!=-1:
    if order<5 and order>=0:
        checkout=checkout+price[order-1]
    else:
        print("Invalid")
    order = int(input("What is your order (1-5): "))
print("Checkout:", checkout)