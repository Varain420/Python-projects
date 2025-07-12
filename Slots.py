import random


def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','🌟']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))
def get_payout(row, bet):
   if row[0] == row[1] == row[2]:
       if row[0] == '🍒':
           return bet * 3
       elif row[0] == '🍉':
           return bet * 4
       elif row[0] == '🍋':
           return bet * 5
       elif row[0] == '🔔':
           return bet * 6
       elif row[0] == '🌟':
           return bet * 10

   return 0
def main():

    balance = 100
    print("***********************")
    print("Welcome to Python slots")
    print("Symbols:🍒 🍉 🍋 🔔 🌟")
    print("***********************")
    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid amount.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Sorry, you don't have enough money.")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Your payout: ${payout}")
        else:
            print("Sorry, you don't have enough money.")

        balance += payout


        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    print(f"Thank you for playing! Your final balance is  ${balance}")
if __name__ =='__main__':
     main()