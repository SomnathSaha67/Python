student={"name":"ravi","marks":{"physics":88,"chemistry":90,"maths":92},"age":20}
print(student)
print(student["marks"]["maths"])
student["marks"]["chemistry"]=88
print(f"Updated after changing chemistry marks: {student}")
student["marks"]["english"]=92
print(f"Updated after adding english marks: {student}")