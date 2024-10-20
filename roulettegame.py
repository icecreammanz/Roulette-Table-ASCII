from random import randint
from time import sleep
from colorama import Fore, Back, Style, init
import random

init(autoreset=True)


def firstrow():
    firstrows = []
    skip_next = False
    for x in range(3, 37):
        if x % 3 == 0 and not skip_next:
            firstrows.append(Back.BLACK + str(x).ljust(2))
            skip_next = True
        elif x % 3 == 0 and skip_next:
            firstrows.append(Back.RED + str(x).ljust(2))
            skip_next = False
    return " | ".join(firstrows)


def secondrow():
    secondrows = []
    start = 2
    while start < 36:
        if start % 2 == 0:
            secondrows.append(Back.RED + str(start).ljust(2))
        else:
            secondrows.append(Back.BLACK + str(start).ljust(2))
        start += 3
    return " | ".join(secondrows)


def thirdrow():
    thirdrows = []
    start = 1
    while start < 35:
        if start % 2 == 0:
            thirdrows.append(Back.RED + str(start).ljust(2))
        else:
            thirdrows.append(Back.BLACK + str(start).ljust(2))
        start += 3
    return " | ".join(thirdrows)


def tableshow(firstrow, secondrow, thirdrow):
    print("+-----+-----------------------------------------------------------+")
    print("|     |               Roulette Table                              |")
    print("+-----+-----------------------------------------------------------+")
    print(f"|     | {firstrow} |")
    print(f"|  0  | {secondrow} |")
    print(f"|     | {thirdrow} |")
    print("+-----+-----------------------------------------------------------+")
    print("|     |       1ST12       |       2ND12       |        3RD12      |")
    print("+-----+-----------------------------------------------------------+")
    print("|     |  1TO18  |   EVEN  |   RED   |  BLACK  |   ODD  |  19TO36  |")
    print("+-----+-----------------------------------------------------------+")


def getpayout(holder, bet, winning_color, winning_ods, winning_number):

    if str(winning_number) in holder :
        return bet * 32
    if winning_color in holder:
        return bet * 2
    if winning_ods in holder:
        return bet * 2
    return 0

def main():
    balance = 1000
    firstrows = firstrow()
    secondrows = secondrow()
    thirdrows = thirdrow()

    colors = ['Red', 'Black']
    playing = True

    while balance > 0 and playing:
        tableshow(firstrows, secondrows, thirdrows)
        print(f"Current balance: ${balance}")

        bet = input("Enter bet amount: ")
        if not bet.isdigit():
            print("Invalid amount. Please enter a numeric value.")
            continue
        bet = int(bet)
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        if bet > balance:
            print("Bet exceeds your balance.")
            continue

        balance -= bet
        sleep(0.1)
        tableshow(firstrows, secondrows, thirdrows)
        print(f"Bet amount: ${bet}")
        holder = []
        betting = True
        while betting:
            place = input("Place your bets (Q or finalize) : ").capitalize()

            if place.isdigit() and 0 <= int(place) <= 36:
                holder.append(place)
                continue
            elif place in ['Red', 'Black', 'Even', 'Odd']:
                holder.append(place)
                continue

            elif place == 'Q':
                winning_color = random.choice(colors)
                winning_number = random.randint(0 , 37)
                winning_ods = None
                if winning_number % 2 == 0:
                    winning_ods = 'Even'
                elif not winning_number % 2 == 0:
                    winning_ods = 'Odd'
                print("\nSpinning...")
                sleep(1)
                payout = getpayout(holder, bet, winning_color, winning_ods, winning_number)

                if payout > 0:
                    print(f"\n🎉 Congratulations 🎉 You won ${payout}\n")
                    balance += payout
                else:
                    print(f"\nYou lost ${bet}\n")

                print(f"Winning spin was {winning_number} {winning_color}")
                print(f"Current balance is ${balance}")
                betting = False

            else:
                print("Invalid bet. Please try again.")

        choices = input("\nDo you want to play again (Y/N)? ").capitalize()
        while choices not in ['Y', 'N'] :
            choices = input("\nDo you want to play again (Y/N)? ").capitalize()

        if choices == 'N':
            playing = False
    if not playing and balance > 0:
        print("\nThank you for playing...")
    elif not playing and balance == 0:
        print("\nThank you for playing...")
    else:
        print("\nInsufficient funds")

if __name__ == '__main__':
    main()
