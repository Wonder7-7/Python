print("-----WELCOME TO STEVE'S SURVEY-----")
print("-----ONLY ACCESSIBLE TO 18 YEARS AND ABOVE-----!")

age=int(input("Enter your age: "))

if age>=18:
    print("Welcome to the SURVEY!")

    input("Press enter to continue.")

    Q1 = input("Have you been in a relationship recently? ")
    if Q1 == "Yes" or Q1 == "Yes i have" or Q1 == "yes":
        Q2=input("How is it going? ")
        print("Interesting.")
        Q3=input("What are you doing to keep it going? ")
        input("I see. All the best in your relationship. press enter to end")
    else:
        A1=input("Do you plan on being in one soon? ")
        if A1 == "No" or A1 == "no":
            input("What is your reason behind it? ")
            input("Okay. Good luck and all the best! Press enter to end")
        else:
            input("Great to hear. Wishing you all the best. Press enter to end")

else:
    input("Sorry, you are not eligible for the survey.")




