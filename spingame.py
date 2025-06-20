import random

def spin_row():
    symbols = ['🍉', '🍒', '🥭', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print()
    print(" | ".join(row))
    print()

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        if symbol == '🍉':
            return bet * 3
        elif symbol == '🍒':
            return bet * 4
        elif symbol == '🥭':
            return bet * 5
        elif symbol == '🔔':
            return bet * 10
        elif symbol == '⭐':
            return bet * 20
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet * 2  # partial match
    else:
        return 0

def main():
    balance = 100

    print("\nWelcome to Python Slots!")
    print("Symbols: 🍉 🍒 🥭 🔔 ⭐\n")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number\n")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds\n")
            continue
        if bet <= 0:
            print("Bet must be greater than 0\n")
            continue

        print("\nSpinning...\n")
        balance -= bet
        row = spin_row()
        print_row(row)
        payout = get_payout(row, bet)


        if payout > 0:
            print(f"You won ${payout}!\n")
        else:
            print("No match. Try again!\n")
        balance += payout
        play_again=input("Do you want to spin again?(Y/N):").upper()
        if play_again!='Y':
            break

    print(f"Game over! You're out of money.Your balance is ${balance} 💸")

if __name__ == '__main__':
    main()
