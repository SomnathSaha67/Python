weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))    
bmi=weight/(height**2)
bmi_category="Underweight" if bmi<18.5
bmi_category="Normal weight" if 18.5<=bmi<24.9
bmi_category="Overweight" if 25<=bmi<29.9
bmi_category="Obesity" if bmi>=30
print(f"Your BMI is {round(bmi, 2)}, which is considered: {bmi_category}.")