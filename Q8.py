#WAP to accept a number and print all its factors.

num=int(input("Enter a number: "))
if num==0:
    print("Every non-zero integer is a factor of 0")
else:
    print(f"The factors of {num} are:")
    for i in range(1,num+1):
        if num%i==0:
            print(i)