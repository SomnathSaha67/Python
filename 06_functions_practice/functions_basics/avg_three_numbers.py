def average_marks(m1,m2,m3):
    avg=(m1+m2+m3)/3
    return avg
mark1=float(input("Enter marks of subject 1: "))
mark2=float(input("Enter marks of subject 2: "))
mark3=float(input("Enter marks of subject 3: "))
print(f"Average marks of three subjects is: {average_marks(mark1,mark2,mark3)}")