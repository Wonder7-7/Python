while True:
    name=input("What is your name?\nBegin with a capital letter: ")
    if name == "Steve":
        while True:
            age = input("How old are you? ")
            if age == "19":
                print("Nice to meet you! "+name)
                print("You are "+age+" years old.")
                break
            else:
                print("That is not your age.\nTry again.")
        break
    else:
        print("That is not your name.")

