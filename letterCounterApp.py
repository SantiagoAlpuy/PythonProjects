app_name = "Letter Counter"
print(f"Welcome to the {app_name} App",end="\n")

name = input('What is your name? ')
print(f'Its nice to have you here {name}!',end='\n')
phrase = input("Give us a phrase: ")
print()
letter = input('Which letter do you want to count? ')
print()
cnt = phrase.lower().count(letter)
print(f'There are {cnt} occurrences of the letter "{letter}"')
