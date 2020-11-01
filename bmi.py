bmi = int
weight = input("Your weight in kilogram: ")
weight = float(weight) # Converting weight to a float
size = input("Your Size in meters: ")
size = float(size) # Conerting size to a float
size = size ** 2 # squaring size by 2
bmi = weight / size # bmi = weight / size^2
bmi = round(bmi, 1) # Round the bmi by 2 after decimal point
print("Your BMI is", bmi) # Printing out your BMI
