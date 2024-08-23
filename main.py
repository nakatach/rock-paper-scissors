import getpass

score = [0,0]
print("Welcome to Rock Paper Scissors Game! The Score Starts at", score)

while True:
    player1 = getpass.getpass(prompt="Enter your choice (r/p/s): ")
    player2 = input("Enter your coice (r/p/s): ")

    if player1.lower() in ["r"]:
        if player2.lower() in ["s"]:
            score[0] += 1
            print("Player 1 win! The score is now", score)
        elif player2.lower() in ["r"]:
            print("It's a tie! The score remains", score)
        elif player2.lower() in ["p"]:
            score[1] += 1
            print("Player 2 win! The score is now", score)

    if player1.lower() in ["p"]:
        if player2.lower() in ["r"]:
            score[0] += 1
            print("Player 1 win! The score is now", score)
        elif player2.lower() in ["p"]:
            print("It's a tie! The score remains", score)
        elif player2.lower() in ["s"]:
            score[1] += 1
            print("Player 2 win! The score is now", score)

    if player1.lower() in ["s"]:
        if player2.lower() in ["p"]:
            score[0] += 1
            print("Player 1 win! The score is now", score)
        elif player2.lower() in ["s"]:
            print("It's a tie! The score remains", score)
        elif player2.lower() in ["r"]:
            score[1] += 1
            print("Player 2 win! The score is now", score)
        
    play_again = input("Want to play again? (y/n): ")
    if play_again != "y":
        print("Thank you for playing!")
        break