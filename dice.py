import random
import json

def calculate_payout(range_size):
    return 99 / range_size

def load_profile():
    try:
        with open("profiles.json", "r") as file:
            return json.load(file)
    except FilenotFoundError:
        return{}

def main():
    print("Welcome to the Dice Game!")
    balance = 100 

    while True:
        print(f"Your current balance is: ${balance:.2f}")
        try:
            bet = float(input("Enter your bet amount: "))
            if bet <= 0 or bet > balance:
                print("Invalid bet amount. Please enter an amount within your current balance.")
                continue

            lower_bound = int(input("Enter the lowest number in your range (1-100): "))
            upper_bound = int(input("Enter the highest number in your range (1-100): "))
            
            if lower_bound < 1 or upper_bound > 100 or lower_bound >= upper_bound:
                print("Wrong range. Please enter a number between 1 and 100, and make sure the lower number is less than the highest number.")
                continue

            range_size = upper_bound - lower_bound + 1
            payout = calculate_payout(range_size)

            print(f"Your range is {lower_bound} to {upper_bound}.")
            print(f"Your potential payout multiplier is {payout:.2f}")

            roll = random.randint(1, 100)
            print(f"The dice rolled: {roll}")

            if lower_bound <= roll <= upper_bound:
                winnings = bet * payout
                balance += winnings
                print(f"Congratulations! You win ${winnings:.2f}! Your new balance is ${balance:.2f}.")
            else:
                balance -= bet
                print(f"Sorry, you lose ${bet:.2f}. Your new balance is ${balance:.2f}.")

            if balance <= 0:
                print("You have run out of balance. Game over!")
                break

            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
