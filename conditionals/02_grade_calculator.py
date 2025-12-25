marks=float(input("Enter your marks (0-100): "))
grade="A" if 90<= marks <=100
grade="B" if 80<= marks <90 
grade="C" if 70<= marks <80
grade="D" if 60<= marks <70
grade="F" if 0<= marks <60
grade="Invalid" if marks <0 or marks >100
print(f"Your grade is: {grade}.")