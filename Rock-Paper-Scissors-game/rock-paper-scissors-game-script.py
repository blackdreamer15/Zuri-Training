import random

print("**********************************************")
print("*    ROCK PAPER SCISSOR GAME USING PYTHON    *")
print("**********************************************\n")

# CHOOSE TO SEE INSTRUCTIONS BEFORE GAME BEGINS
initialInput = int(input("Enter 1 to see the instructions and 2 to skip ::  "))
if(initialInput==1):
    print("\n\nWhen the game starts, just enter R for Rock, P for Paper and S for Scissor\nWinning Rules of the Rock paper scissor game as follows: \n"
            +"Rock(R)  vs  Paper(P)    ->  Paper(P) wins \n"
            +"Rock(R)  vs  Scissor(S)  ->  Rock(R) wins \n"
            +"Paper(P) vs  Scissor(S)  ->  Scissor(S) wins \n")

# List of options
optionList = ['R', 'P', 'S']

# Taking user's choice and randomize computer's choice
userChoice = input("Enter your choice (R for rock, P for paper, S for scissors) ::\t")
computerChoice = random.choice(optionList)

# Print the choice made
print("\nYou chose ", userChoice, " and computer chose ", computerChoice, ".\n")


