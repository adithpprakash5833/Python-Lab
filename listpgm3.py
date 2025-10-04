nums=input("enter a list of integers seperatd by space:").split()
result=[]
for n in nums:
    n=int(n)
    if n>100:
        result.append("over")
    else:
        result.append(n)
print(result)