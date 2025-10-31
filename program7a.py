def calculate(p,n,r):
    s=(p*n*r)/100
    print("simple interest=",s)
age=int(input("Enter your age:"))
p=int(input("Enter the principle amount:"))
n=int(input("Enter the number of years:"))

if age < 60:
    r=10
else:
    r=12
print("Rate of interest:",r)
calculate(p,n,r)