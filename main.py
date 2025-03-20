import random

options = ("rock", "paper", "scissors")
is_running = True
play_again = ""
  
while is_running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
            is_running = False
        else:
            print("You lose! Game over!")    
            play_again == input("Play again (y/n): ").lower()
            if not play_again=="y":
                is_running = False

print("Thanks for playing!")


