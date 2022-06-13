import random, sys, os

# List of options
optionList = ['R', 'P', 'S']

while True:
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
    
    # Taking user's choice and randomize computer's choice
    computerChoice = random.choice(optionList)
    userChoice = input("Enter your choice (R for rock, P for paper, S for scissors) ::  ").upper()
    
    # Print the choice made
    print("\nYou chose ", userChoice, " and computer chose ", computerChoice, ".\n")


    # CHECK TO SEE THE OUTCOME
    if userChoice == computerChoice:
        print("It's a tie!\n")
        
    elif(userChoice == 'R'):
        if computerChoice == 'S':
            print(" You win!Rock smashes scissors!\n")
        else:
            print("You lose! Paper covers rock!\n")

    elif(userChoice == 'P'):
        if computerChoice == 'R':
            print(" You win!Paper covers rock!\n")
        else:
            print("You lose! Scissors cuts paper!\n")

    elif(userChoice == 'S'):
        if computerChoice == 'P':
            print("You win! Scissors cuts paper!\n")

    #CHECK IF USER WISHES TO PLAY AGAIN
    ans = input("Do you want to play again? (Y/N) :: ").lower()
 
    # if user input n or N then condition is False
    if (ans == 'n'):
        break
    elif(ans=='y'):
        os.system('cls');
     
# after coming out of the while loop
print("\nThanks for playing")
