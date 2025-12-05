s1={1,2,3,4,5}
s2={4,5,6,7,8}
s_union=s1.union(s2)
print(f"Union of {s1} and {s2} is {s_union}")
s_union_operator=s1 | s2
print(f"Union using '|' operator: {s_union_operator}")  
s_intersection=s1.intersection(s2)
print(f"Intersection of {s1} and {s2} is {s_intersection}")
s_intersection_operator=s1 & s2
print(f"Intersection using '&' operator: {s_intersection_operator}")
diff_s1_s2=s1.difference(s2)
print(f"Difference of {s1} and {s2} is {diff_s1_s2}")
diff_s1_s2_operator=s1 - s2
print(f"Difference using '-' operator: {diff_s1_s2_operator}") 
diff_s2_s1=s2.difference(s1)
print(f"Difference of {s2} and {s1} is {diff_s2_s1}")
diff_s2_s1_operator=s2 - s1
print(f"Difference using '-' operator: {diff_s2_s1_operator}")