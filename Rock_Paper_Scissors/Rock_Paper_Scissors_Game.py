import random


def get_user_choice():
    user_choice = input("Choose rock, paper or scissors : ").lower()
    return user_choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice


def winner(user_choice, computer_choice, user_score, computer_score):
    if user_choice == computer_choice:
        print("It's tie!")
        user_score += 1
        computer_score += 1

    elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer Win!")
        computer_score += 1

    return user_score, computer_score


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        user_score, computer_score = winner(user_choice, computer_choice, user_score, computer_score)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Final scores: You {user_score} - {computer_score} Computer")


if __name__ == "__main__":
    main()

