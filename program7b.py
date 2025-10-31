def check(num):
    if num % 2==0:
        return"Even"
    else:
        return"Odd"
num=int(input("Enter the number:"))
print("The given number",num,"is",check(num))