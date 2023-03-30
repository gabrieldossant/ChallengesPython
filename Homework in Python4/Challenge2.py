'''
    Write a program in Python that implements a calculator with the functions add, 
    subtract, multiply, and divide. The program should prompt the user for the two 
    values, and ask for the desired operation ('+', '-' , '*' or '/' ) and then
    calculate and display the result.
'''
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
print("Choose an operator to calculate:")
op = input("(+) (-) (*) (/)")

if op == "+":
    print(f"Sum result: {n1 + n2}")
elif op == "-":
    print(f"Subtraction result: {n1 - n2}")
elif op == "*":
    print(f"Multiplication result: {n1 * n2}") 
elif op == "/":
    print(f"Division result: {n1 / n2}")
else:
    print("Invalid operator | Try Again")