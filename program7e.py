def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("sum is",sum)
input_number=input("Enter integers seperated by spaces:").split()
input_number=[int(num) for num in input_number]
result=add(*input_number)