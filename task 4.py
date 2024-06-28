import random

def user_choice():
    options = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please select rock, paper, or scissors.")

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def show_results(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to the Rock, Paper, Scissors game!")

    while True:
        user = user_choice()
        computer = computer_choice()
        winner = decide_winner(user, computer)
        show_results(user, computer, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score}")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()
