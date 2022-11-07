# Alex Goussatchok
# QA 4822
# Task: Ordered view of elements
# v 1.0

# The probability of randomly list generated to be sorted is pretty low.... input less items in list when prompted

import random

MIN_RANGE = 1
MAX_RANGE = 100


def input_number_of_items_in_sequence():
    items_num = int(input("Enter a number of items in sequence: "))
    return items_num


def generate_sequence(items_num):
    sequence = []
    for _ in range(items_num):
        sequence.append(random.randint(MIN_RANGE, MAX_RANGE))
    return sequence


def check_if_sequence(sequence):
    flag = 0
    if all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1)) \
            or all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1)):
        flag = 1
    return flag


def user_output(msg):
    print(msg)


def main():
    items_num = input_number_of_items_in_sequence()
    sequence = generate_sequence(items_num)
    flag = check_if_sequence(sequence)
    msg = f"The sequence {sequence} is sorted" if flag == 1 else f"The sequence {sequence} is not sorted"
    user_output(msg)


main()
