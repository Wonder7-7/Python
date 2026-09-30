#WAP to accept a word from the user and count the number of vowels in it.

word=input("Enter a word: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for char in word:
    if char in vowels:
        count+=1
print(f"There are {count} vowels in {word}")