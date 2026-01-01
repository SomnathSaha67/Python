marks=int(input("Enter your marks (0-100): "))
match marks:
    case m if 90 <= m <= 100:
        grade="A"
    case m if 80 <= m < 90:                     
        grade="B"
    case m if 70 <= m < 80:
        grade="C"
    case m if 60 <= m < 70:
        grade="D"
    case m if 0 <= m < 60:
        grade="F"
    case _:
        grade="Invalid marks"
print(f"Grade: {grade}")