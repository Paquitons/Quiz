import os, sys, time
os.system('cls')
incorrect = 0;
finalgrade = "0%"

print("Welcome to Paq's Quiz!")
print("")
question = input("Do you wanna play? y/n: ")
if question == "y":
    print("Ok")
    print("")
else:
    sys.exit()
os.system('cls')
question1 = input("What does GPU stand for? ")
if question1 == "Graphics Processing Unit":
    print("Correct!")
elif question1 == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    incorrect += 1

print("")

question2 = input("What does CPU stand for? ")
if question2 == "Central Processing Unit":
    print("Correct!")  
elif question2 == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    incorrect += 1

print("")

question3 = input("Who made this quiz? ")
if question3 == "Paq" or question3 == "paq":
        print("Correct")
else:
    print("Incorrect!")
    incorrect += 1


print("")

print("Total of " + str(incorrect) + " questions incorrect!")

print("")

if incorrect == 3:
    finalgrade = "0%"
elif incorrect == 2:
    finalgrade = "33%"
elif incorrect == 1:
    finalgrade == "67%"
elif incorrect == 0:
    finalgrade = "100%"

print("You got a " + finalgrade)

time.sleep(3)
os.system('cls')

end = input("Press enter to exit.")
os.system('cls')
