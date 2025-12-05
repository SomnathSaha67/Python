a={1,2,3,4,5}
b={4,5,6,7,8}
diff_ab=a.difference(b)
print(f"Difference of {a} and {b} is {diff_ab}")
diff_ab_operator=a - b
print(f"Difference using '-' operator: {diff_ab_operator}") 
diff_ba=b.difference(a)
print(f"Difference of {b} and {a} is {diff_ba}")
diff_ba_operator=b - a
print(f"Difference using '-' operator: {diff_ba_operator}")