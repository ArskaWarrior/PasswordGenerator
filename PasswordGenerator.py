#PasswordGenerator
import random
letterCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numberCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialCharacters = ['~','`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', '<', ',', '>', '.', '?', '/']

#Question before starting
size = int(input("How long should password be? "))
letters = input("Y/N, letters? ")
numbers = input("Y/N, numbers? ")
special = input("Y/N, specialCharacters? ")

#List of what to add and needs to be added
typesToAdd = []
typesToAddForcer = []
if letters.lower() == "y":
    typesToAdd.append("letter")
    typesToAddForcer.append("letter")
if numbers.lower() == "y":
    typesToAdd.append("number")
    typesToAddForcer.append("number")
if special.lower() == "y":
    typesToAdd.append("special")
    typesToAddForcer.append("special")


repeat = True
while repeat:
    word = ""
    for i in range(size):
        if len(typesToAddForcer) > 0:#Charactertypes to be added forcefully
            index = random.randint(0, len(typesToAddForcer) - 1)
            if typesToAddForcer[index] == "letter":
                word += letterCharacters[random.randint(0, len(letterCharacters) - 1)]
                typesToAddForcer.pop(index)
            elif typesToAddForcer[index] == "number":
                word += numberCharacters[random.randint(0, len(numberCharacters) - 1)]
                typesToAddForcer.pop(index)
            elif typesToAddForcer[index] == "special":
                word += specialCharacters[random.randint(0, len(specialCharacters) - 1)]
                typesToAddForcer.pop(index)
        else: #Random characters from the list
            index = random.randint(0, len(typesToAdd) - 1)
            if typesToAdd[index] == "letter":
                word += letterCharacters[random.randint(0, len(letterCharacters) - 1)]
            elif typesToAdd[index] == "number":
                word += numberCharacters[random.randint(0, len(numberCharacters) - 1)]
            elif typesToAdd[index] == "special":
                word += specialCharacters[random.randint(0, len(specialCharacters) - 1)]
    print("Generated password: ")
    print(str(word))
    
    #Repeating, if you are not happy with your password
    repeatQuestion = str(input("Repeat Y/N: ")).lower()
    if  repeatQuestion == "y" or repeatQuestion == "":
        repeat = True
    else:
        repeat = False