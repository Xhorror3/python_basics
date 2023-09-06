weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in meter:"))

bmi = round(weight/(height**2))

if bmi<18.5:
    print(f"Your bmi is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi} and you are normal.")
elif bmi < 30:
    print(f"Your bmi is {bmi} and you are overweight.")
else:
    print(f"Your bmi is {bmi} and you are obese")