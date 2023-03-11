import random

def play_game():
    game = True
    figures = ("paper", "rock", "scissors")
    computer_choice = (random.choice(figures))
    print("""
        Welcome to the classic game!
    It's called Paper, rock, scissors!
      created by Maciej Smulski for Z2J""")
    print()
    player_choice = input("Choose one of the available options: paper, rock or scissors!: ")
    while player_choice not in ("paper", "rock", "scissors"):
        player_choice = input("Wrong answer. Try again: ")
    else:
        print()
        print("Your choice is: " + player_choice +"!")
        print()
        print("Computer choose: " + computer_choice +"!")
        print()
    if player_choice == "paper":
        if computer_choice == "paper":
            print("DRAW!")
        elif computer_choice == "rock":
            print("YOU WIN!")
        else:
            print("YOU LOOSE!")
    if player_choice == "rock":
        if computer_choice == "paper":
            print("YOU LOOSE!")
        elif computer_choice == "rock":
            print("DRAW!")
        else:
            print("YOU WIN!")
    if player_choice == "scissors":
        if computer_choice == "paper":
            print("YOU WIN!")
        elif computer_choice == "rock":
            print("YOU LOOSE!")
        else:
            print("DRAW!")
    print()
    play_again = input("Do you want to play again? If so, type 'again', if not, type 'exit': ")
    if play_again == "again":
        play_game()
    elif play_again == "exit":
        game = False

play_game()
