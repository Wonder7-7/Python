#WAP to accept a number and check whether it is positive, negative or zero.

num = int(input("Enter a number: "))

if num>0:
    print(f"{num} is a positive number.")
elif num==0:
    print(f"{num} is an empty number.")
else:
    print(f"{num} is a negative number.")