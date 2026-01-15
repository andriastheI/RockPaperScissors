"""
Filename: rock_paper_scissors.py
Author: Andrias Zelele
Date: 2026-01-13
Description:
    This program implements a console-based Rock Paper Scissors game
    where a user plays against the computer. The game supports multiple
    rounds, tracks statistics, handles ties correctly, and allows the
    user to replay the game.
Sources: None (original work)
"""

import time
import random


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
def main():
    intro()
    run_game()


# ------------------------------------------------------------
# Displays the introduction and game instructions
# ------------------------------------------------------------
def intro():
    print("Welcome to the Rock Paper Scissors game!")
    time.sleep(2)
    print("In this game you will be playing against the computer")
    time.sleep(2)
    print("You are only allowed to choose a rock('r'), paper('p'), or scissors('s').")
    time.sleep(2)
    print("First you will be prompted to choose the number of rounds of the game.")
    time.sleep(2)
    print("After you finish every game, the stats board will be printed.")
    time.sleep(2)
    print("A tie will be counted and displayed on the stats board but will not be counted towards the game rounds")
    time.sleep(2)
    print("Good Luck")


# ------------------------------------------------------------
# Controls overall program flow and replay logic
# ------------------------------------------------------------
def run_game():
    if not verify_playing():
        print("Good Game!")
        return

    while True:
        play()

        again = input("Would you like to play again ?(y/n). ").strip().lower()
        while again not in ("y", "n"):
            again = input("Please enter either 'y' or 'n': ").strip().lower()

        if again == "n":
            break

    print("Good Game!")



# ------------------------------------------------------------
# Controls one full game session
# ------------------------------------------------------------
def play():
    number_of_rounds = round_prompt()

    print("Best of " + str(number_of_rounds))

    count = 0
    computer_win_count = 0
    player_win_count = 0
    tie_count = 0

    while number_of_rounds > 0:
        count += 1

        print("     ROUND: " + str(count))
        print("PLAYER: " + str(player_win_count))
        print("COMPUTER: " + str(computer_win_count))
        print("TIE: " + str(tie_count))

        while True:
            player = input("Rock(r), Paper(p), Scissors(s)? ").strip().lower()
            if player == "r":
                player = "Rock"
                break
            elif player == "p":
                player = "Paper"
                break
            elif player == "s":
                player = "Scissors"
                break
            else:
                print("Please enter either 'r' or 'p' or 's'.")

        computer = rand_com_choice()
        print("")
        print("Computer chose: " + str(computer))
        print("Player chose: " + str(player))

        winner = check_win(computer, player)

        if winner == "0":
            computer_win_count += 1
            number_of_rounds -= 1
            print("Computer wins this round!")
        elif winner == "1":
            player_win_count += 1
            number_of_rounds -= 1
            print("Player wins this round!")
        else:
            tie_count += 1

    print("TOTAL ROUNDS : " + str(count))
    print("PLAYER: " + str(player_win_count))
    print("COMPUTER: " + str(computer_win_count))
    print("TIE: " + str(tie_count))

    if computer_win_count > player_win_count:
        print("****************************")
        print("***** COMPUTER WINS! *******")
        print("****************************")
    else:
        print("****************************")
        print("***** PLAYER WINS! *******")
        print("****************************")


# ------------------------------------------------------------
# Prompts user to choose the number of rounds
# ------------------------------------------------------------
def round_prompt():
    print("Choose the number of round you want to play: ")
    print("(a) Best of 1")
    print("(b) Best of 3")
    print("(c) Best of 5")

    while True:
        rounds = input(" ").strip().lower()
        if rounds == "a":
            return 1
        elif rounds == "b":
            return 3
        elif rounds == "c":
            return 5
        else:
            print("Please enter either 'a' or 'b' or 'c'.")



# ------------------------------------------------------------
# Asks the player if they want to start the game
# ------------------------------------------------------------
def verify_playing():
    while True:
        begin = input("Would you like to start the game?(y/n). ").strip().lower()
        if begin == "y":
            return True
        elif begin == "n":
            print("Thank you for not playing!")
            return False
        else:
            print("Please enter either 'y' or 'n'.")


# ------------------------------------------------------------
# Determines the winner of a round
# ------------------------------------------------------------
def check_win(ply1, ply2):
    if ply1 == "Rock" and ply2 == "Scissors":
        return "0"
    elif ply1 == "Rock" and ply2 == "Paper":
        return "1"
    elif ply1 == "Paper" and ply2 == "Rock":
        return "0"
    elif ply1 == "Paper" and ply2 == "Scissors":
        return "1"
    elif ply1 == "Scissors" and ply2 == "Rock":
        return "1"
    elif ply1 == "Scissors" and ply2 == "Paper":
        return "0"
    else:
        return "-1"


# ------------------------------------------------------------
# Generates a random choice for the computer
# ------------------------------------------------------------
def rand_com_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


# ------------------------------------------------------------
# Program execution
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
