# Alex Goussatchok
# QA 4822
# Task: Even & Odd numbers count
# v 1.0
import random

MIN_NUMBER_OF_NUMS_IN_SEQUENCE = 2
MAX_NUMBER_OF_NUMS_IN_SEQUENCE = 10

MIN_NUMBER_IN_SEQUENCE = 1
MAX_NUMBER_IN_SEQUENCE = 100


def number_of_nums_in_sequence():
    number_of_nums = random.randint(MIN_NUMBER_OF_NUMS_IN_SEQUENCE, MAX_NUMBER_OF_NUMS_IN_SEQUENCE)
    return number_of_nums


def create_sequence(number_of_nums):
    sequence = []
    while len(sequence) < number_of_nums:
        num = random.randint(MIN_NUMBER_IN_SEQUENCE, MAX_NUMBER_IN_SEQUENCE)
        sequence.append(num)
    return sequence


def calculate_evens_odds(sequence):
    evens_count = 0
    odds_count = 0
    for i in sequence:
        if i % 2 == 0:
            evens_count += 1
        elif i % 2 > 0:
            odds_count += 1
    return evens_count, odds_count


def user_output(msg):
    print(msg)


def main():
    number_of_nums = number_of_nums_in_sequence()
    sequence = create_sequence(number_of_nums)
    evens_count, odds_count = calculate_evens_odds(sequence)
    msg = f"In the sequence {sequence}:\nThe number of evens is {evens_count}\nThe number of odds is {odds_count}"
    user_output(msg)


main()
