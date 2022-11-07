# Alex Goussatchok
# QA 4822
# Task: Float number sequence
# v 1.0

# without conversion of sequence to tuple type somehow the order of numbers changes (it becomes similar
# to changed_sequence numbers order while changing places of min & max value numbers, sus tuple is not
# changeable everything goes fine, but it requires changed_sequence type change to list


import random

# we need these constant variables to make the script scalable
MIN_RANGE = -100
MAX_RANGE = 100
ROUND_FLOAT = 2


def input_number_of_items_in_sequence():
    items_num = int(input("Enter a number of items in sequence: "))
    return items_num


def generate_sequence(items_num):
    sequence = []
    for _ in range(items_num):
        sequence.append(round(random.uniform(MIN_RANGE, MAX_RANGE), ROUND_FLOAT))
    return tuple(sequence)


def find_sequence_min_value(sequence):
    for element in range(len(sequence)):
        min_value = min(sequence)
    return min_value


def find_max_value(sequence):
    for element in range(len(sequence)):
        max_value = max(sequence)
    return max_value


def calculate_average(sequence):
    average = 0
    for element in sequence:
        average += element
    return round(average / len(sequence), ROUND_FLOAT)


def calculate_values(sequence):
    negatives, positives, zero = 0, 0, 0
    for element in sequence:
        if element < 0:
            negatives += 1
        elif element > 0:
            positives += 1
        elif element == 0:
            zero += 1
    return negatives, positives, zero


def change_extreme_values_positions(sequence, min_value, max_value):
    changed_sequence = sequence
    changed_sequence = list(changed_sequence)
    for element in range(len(changed_sequence)):
        if changed_sequence[element] == max_value:
            changed_sequence[element] = min_value
        elif changed_sequence[element] == min_value:
            changed_sequence[element] = max_value
    return changed_sequence


def user_output(msg):
    print(msg)


def main():
    items_num = input_number_of_items_in_sequence()
    sequence = generate_sequence(items_num)
    min_value = find_sequence_min_value(sequence)
    max_value = find_max_value(sequence)
    average = calculate_average(sequence)
    negatives, positives, zero = calculate_values(sequence)
    changed_sequence = change_extreme_values_positions(sequence, min_value, max_value)
    msg = f"The list of generated numbers is {sequence}:\n\n" \
          f"The minimal number value is:  {min_value}, " \
          f"the maximum number value is: {max_value}\n\n" \
          f"The average summary of numbers is: {average}\n\n" \
          f"The number of negative numbers is: {negatives}, " \
          f"the number of Zeros is: {zero} " \
          f"the number of positive number is: {positives}\n\n" \
          f"The list with min & max value numbers positions change is: {changed_sequence}"
    user_output(msg)


main()
