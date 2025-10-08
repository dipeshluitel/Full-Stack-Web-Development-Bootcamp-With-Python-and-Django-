from random import randint

def checkGuess(guess,rnum):
    for i in range(3):
        if guess[i]==rnum[i]:
            return ("Match")
        elif guess[i] in rnum:
            return ("Close")

    return "Nope"

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!\nCode has been generated, please guess a 3 digit number")

random_number = str(randint(100,999))
status = "ON"
while status == "ON":
    guess = (input("What is your Guess? "))

    if(len(guess)==3 and guess.isdigit()):
        result = checkGuess(guess,random_number)
        print(result)
        if guess == random_number:
            print(f"You have guessed all the digits correctly! {random_number}")
            status = "OFF"
    else:
        print("Enter Valid 3 digits number")

