typeOfDaily = input("Enter a type daily of hosting: ")
quantyOfDaily = float(input("Enter quanty of daily: "))

if typeOfDaily.upper()[0] == "S":
    print(f"Your value of diary is : {255,50 * quantyOfDaily}")
elif typeOfDaily.upper()[0] == "D":
    print(f"Your value of diary is : {305,50 * quantyOfDaily}")
elif typeOfDaily.upper()[0] == "T":
    print(f"Your value of diary is {360,50}")
else:
    print("Type of hosting is invalid!")

       
