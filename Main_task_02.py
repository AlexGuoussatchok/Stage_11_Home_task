# Alex Goussatchok
# QA 4822
# Task: Mirrored vector
# v 1.0
NUMBERS_IN_SEQUENCE = 4


def create_sequence():
    sequence = []
    i = 0
    while i < NUMBERS_IN_SEQUENCE:
        num = int(input("Please enter a number for a sequence: "))
        sequence.append(num)
        i += 1

    return sequence


def check_sequence_if_mirrored(sequence):
    flag = 0
    for i in range(len(sequence)):
        if sequence[i] != sequence[-i - 1]:
            flag = 1
    return flag


def user_output(msg):
    print(msg)


def main():
    sequence = create_sequence()
    flag = check_sequence_if_mirrored(sequence)
    msg = "mirrored" if flag == 0 else "not mirrored"
    user_output(msg)


main()
