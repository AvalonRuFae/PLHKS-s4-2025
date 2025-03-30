price = [39.9, 34.9, 45.9, 40, 79.9]
order = int(input("What is your order (1-5): "))
checkout = 0
while order!=-1:
    if order>0 and order<6:
       checkout=checkout+price[order]
    else:
        print("Invalid")
    order = int(input("What is your order (1-5): "))
print("Checkout:", checkout)
