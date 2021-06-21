import random #random module to generate the dice value (number)
def game(): #This function will operate the game to play

    computer_digit=random.randint(1,6) #Computer will play it's turn and will select it's number
    print("Your Turn")

    # Adding error handling
    try:
        user_digit=int(input("Choose Your Digit: "))
        if user_digit>6 or user_digit<1: #Checking that the user has entered a correct number
            print("Please enter a Digit less than 6\nDice has only 1 to 6 Digits")
            game()
    
        print(f"User's Digit: {user_digit}\nComputer Digit: {computer_digit}\n")
        if computer_digit==user_digit: # Checking that the user had won the game or not
            print("Congrats! You won the Game")
            with open("score.txt", "r") as f: #Reading the won data from the file (first line is for won and second line is for lose)
                won=f.readlines()
                winning=int(won[0])+1
                won[0]=str(winning)
                with open("score.txt", "w") as f:
                    f.writelines(won)
        else:
            print("Oops you lost the Game!!\nBetter Luck Next Time!!")
            with open("score.txt", "r") as f: #Reading the lose data from the file (first line is for won and second line is for lose)
                lose=f.readlines()
                lossing=int(lose[1])+1
                lose[1]=str(lossing)
                with open("score.txt", "w") as f:
                    f.writelines(lose)
    except:
        print("Please enter a valid Digit only")
        game()

    scorecard()


def scorecard(): #This function will tell that how many times user had Won or Loosed the Game
    with open("score.txt") as f:
        myscore=f.readlines()
        won=myscore[0]
        lose=myscore[1]
        print(f"Total Winning: {won} and Total Lose: {lose}")
    main() # Again calling main menu to provide the home screen to the user

def main(): #This function will contain the main body of game
    print("\n*****Welcome to the Dice Roll Game*****\n")
    print("1: Start\n2: Score Card\n3: Instruction\n4: Exit\n")

    # Adding Error Handling
    try:
        option=int(input("Select the Option: "))
        if option==1:
            game()
        elif option==2:
            scorecard()
        elif option==3:
            with open("instruction.txt") as f: # Printing the instruction file data here
                myfile=f.read()
                print(myfile)
            main()
        elif option==4:
            print("Thanks for Playing the Game")
            exit(0)
        else:
            print("Please Select a valid option to Play the Game!!!")
            main()
    except:
        print("Please enter a valid Digit")
        main()

main() # Initializing the Game by calling the main() function of our game here