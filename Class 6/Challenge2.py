animals = ['cat', 'dog', 'rat', 'camel']

for animal in animals:
    print("The word", animal, "have a quantity: ", len(animal))

print("----------------------------------------")

name = "Aline"
for letter in name:
    print(letter)

print("----------------------------------------")

sequence = [0, 1, 2, 3, 4, 5]

for number in sequence:
    print(f"The sequence is {number}")

print("----------------------------------------")

for i in range(30, 101, 2):
    print(i, end=" ")