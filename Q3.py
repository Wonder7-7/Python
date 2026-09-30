#WAP to accept a number and check whether it is even or odd.

num = int(input("Enter a number: "))
if num%2 < 1:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")