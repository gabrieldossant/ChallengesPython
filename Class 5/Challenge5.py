'''
    Create an algorithm that asks the user for the total amount of the purchase and the
    amount of installments to be financed and the system should print the value of each
    according to the interest rates in the table below:
'''

totalPurchases = float(input("Enter the value of total purchases: "))
quantityParcels = int(input("Enter the quantity of parcels: "))
result = 0

if quantityParcels == 2:
    result = totalPurchases/0.3
    print(f"The amount with interest is : {result}")
elif quantityParcels == 4:
    result = totalPurchases/0.7
    print(f"The amount with interest is : {result}")
elif quantityParcels == 6:
    result = totalPurchases/0.9
    print(f"The amount with interest is : {result}")
elif quantityParcels == 8:
    result = totalPurchases/0.12
    print(f"The amount with interest is : {result}")
else:
    print("This value is invalid. Try again!")