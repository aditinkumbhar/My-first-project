n1=2
n2=3
num=n1<n2
print("value of num=",num)
num=n1<n2
print("value of num=",num)
num=n1<=n2
print("value of num=",num)
num=n1>=n2
print("value of num=",num)


a=2<3 and 4>3
print("value of a=",a)
a=2<3 or 4>3
print("value of a=",a)
a=not a
print("value of a=",a)
a=not a
print("value of a=",a)


a=10
b=5
print("a",a)
print("b",b)
print(id(a),id(b))


n=int(input("Enter a number: "))
if n<5:
    print(n,"is less than 5") 

n=int(input("Enter a number: "))
if n<5:
    print(n,"is less than 5")
else:
    print(n,"is not less than 5")

n=int(input("Enter a number: "))
if n<5:
    print(n,"is less than 5")
elif n>5:
    print(n,"is greater than 5")
else:
    print(n,"is equal to 5")