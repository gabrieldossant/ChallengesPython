purchasePrice = float(input("Enter the purchase total: "))
discount = 20
discontAmount = 0
newValue = 0

if purchasePrice > 200:
    discontAmount = (discount/100)* purchasePrice
    newValue = purchasePrice - discontAmount
    print(f"The purchase price was {purchasePrice} That way you get a 20% discount ")
    print(f"That way you get a {discount}% discount")
    print(f"And you will pay only {newValue}")
else:
    print(f"You did not receive a discount ")
    print(f"The value of your purchase is {purchasePrice}")
    