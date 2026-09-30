#WAP to accept a student's marks and print the grade:
#80 and above → A
#60 to 79 → B
#40 to 59 → C
#below 40 → Fail

StudentMark=int(input("Enter student's mark: "))
if StudentMark>=80:
    print(f"A")
elif StudentMark>=60 and StudentMark<=79:
    print(f"B")
elif StudentMark>=40 and StudentMark<=59:
    print(f"C")
else:
    print(f"Fail")