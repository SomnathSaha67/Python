def sum(*nums):
    total=0
    for num in nums:
        total+=num
    return f"Sum of {', '.join(str(num) for num in nums)} is {total}"
print(sum(1,2,3,4,5))
print(sum(10,20))
print(sum(7,14,21))
print(sum(3,6,9,12,15,18))