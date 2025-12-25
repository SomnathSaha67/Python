age=int(input("Enter your age: "))
age_classification="Invalid" if age<0
age_classification="Child" if 0<=age<=12
age_classification="Teenager" if 13<=age<=19
age_classification="Adult" if 20<=age<=64
age_classification="Senior" if age>=65
print(f"You are classified as: {age_classification}.")