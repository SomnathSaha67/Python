year=int(input("Enter a year: "))
is_leap_year="Leap Year" if year % 4 == 0 and (year%100!=0 or year%400==0) else "Not a Leap Year"
print(f"{year} is a {is_leap_year}.")