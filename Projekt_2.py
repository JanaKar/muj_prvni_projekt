"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
Bulls and Cows
author: Jana Karbanova
email: xkarbanovaj@gmail.com
discord: JanaK#0342
"""
import random
import time
from time import strftime
from time import gmtime
from operator import itemgetter
from colorama import Fore

separator = 47 * '-'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
statistics = list()
single_games = tuple()
first_game = 0
playing = True


def generate_number() -> list:
    """generating of guessed number"""
    while True:
        number = (random.sample(numbers, k=4))
        if number[0] == '0':
            continue
        else:
            # print(''.join(number))  # print the guessed number (used as a control)
            return number


def initialization() -> None:
    """intro print for a single game"""
    print("Hi there!", separator,
          "I've generated a random 4 digit number for you.",
          "Let's play a bulls and cows game.", separator, sep="\n")
    print("Enter a number:", separator, sep="\n")


def check_for_zero(checked_number: list) -> bool:
    if checked_number[0] == '0':
        print("The number cannot start with zero('0'):")
        return True


def check_for_amount_no(checked_number: list) -> bool:
    if len(checked_number) != 4:
        print("Error, please enter a 4 digit number:")
        return True


def check_for_duplicates(checked_number: list) -> bool:
    if len(checked_number) != len(set(checked_number)):
        print("Error, number cannot contain duplicates:")
        return True


def check_for_digits(checked_number: list) -> bool:
    digit = True
    if digit:
        for number in checked_number:
            if not number.isdigit():
                digit = False
                print("Error, wrong character:")
                return True


def printing_bulls_cows(checked_number: list, g_number: list, trial: int) -> None:
    bulls = 0
    cows = 0
    for index, number in enumerate(checked_number):
        if number == g_number[index]:
            bulls += 1
        elif number in g_number:
            cows += 1
    if bulls == 1:
        bull_str = "bull"
    else:
        bull_str = "bulls"
    if cows == 1:
        cow_str = "cow"
    else:
        cow_str = "cows"
    print(f"Trial No.: {trial}, {bulls} {bull_str}, {cows} {cow_str}", separator, sep="\n")


def print_single_result(trial: int, time_needed: int) -> None:
    print('Correct, you have guessed the right number in ' + Fore.RED + str(trial),
          'attempt/s' + Fore.RESET, sep="\n")
    print('You needed following time: ' + Fore.RED + strftime("%H:%M:%S", gmtime(time_needed)) + Fore.RESET,
          separator, sep="\n")


def print_all_results(result: list, individual_games: tuple) -> None:
    print(f"Here are your results sorted from the best one:", separator, sep="\n")
    print(f"Guessed number | No. of attempts |    Time ", separator, sep="\n")
    for index, item in enumerate(result):
        if item == individual_games:
            print(Fore.RED + f"{''.join(result[index][0]):<15}| "
                             f"{result[index][1]:^17}| "
                             f"{result[index][2]:>5}s" + Fore.RESET)
        else:
            print(f"{''.join(result[index][0]):<15}| "
                  f"{result[index][1]:^17}| "
                  f"{result[index][2]:>5}s")


def ask_if_continue() -> bool:
    decision = True
    while decision:
        print("Do you want to play again? (Y/N)")
        another_game = input()
        if another_game.upper() == "Y":
            print(separator, sep='\n')
            return True
            # jumps out of this while loop as playing = True and continues with while playing loop as a new game

        elif another_game.upper() == "N":
            print(separator, "See you then next time, bye, bye.....", separator, sep="\n")
            return False
            # this will finish the full game/program

        else:
            print(separator, "Wrong selection.....", separator, sep="\n")
            continue
            # back to the question if to play again


while playing:
    guessed_number = generate_number()
    initialization()
    trial_number = 0
    guessing = True
    start = time.time()

    # single guess
    while guessing:
        user_number = input()

        # change string to list
        list_user_number = list(user_number)

        # checking of user number for inappropriate input
        if check_for_zero(list_user_number) or \
                check_for_amount_no(list_user_number) or \
                check_for_duplicates(list_user_number) or \
                check_for_digits(list_user_number) is True:
            continue

        trial_number += 1

        # comparing of user number and guessed number
        # full user number is correct
        if list_user_number == guessed_number:
            end = time.time()
            time_length = round(end - start)
            print_single_result(trial_number, time_length)

            # saving the parameters of the game
            single_games = (guessed_number, trial_number, time_length)
            statistics.append(single_games)

            # sorting the results of previous games
            sorted_games = sorted(statistics, key=itemgetter(1, 2))

            # printing the list of results when more games than one
            first_game += 1
            if first_game > 1:
                print_all_results(sorted_games, single_games)

            # finishing of single game
            guessing = False

        else:
            # user number not fully correct, counting of bulls and cows and printing
            printing_bulls_cows(list_user_number, guessed_number, trial_number)
            # guessing continues with another single guess since it is still True

    # after the single game finished user decides if he wants to play again
    playing = ask_if_continue()

