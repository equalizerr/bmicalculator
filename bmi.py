bmi = int
weight = input("Your weight in kilogram: ")
weight = float(weight)
size = input("Your Size in meters: ")
size = float(size)
size = size ** 2
bmi = weight / size
bmi = round(bmi, 1)
print("Your BMI is", bmi)
