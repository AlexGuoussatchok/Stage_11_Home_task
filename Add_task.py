# Alex Goussatchok
# QA 4822
# Task: Marks percentage
# v 1.0

import random

NUMBER_OF_MARKS = 30

MIN_MARK = 0
MAX_MARK = 5


def create_list_of_marks():
    marks_list = []
    while len(marks_list) < NUMBER_OF_MARKS:
        mark = random.randint(MIN_MARK, MAX_MARK)
        marks_list.append(mark)
    return marks_list


def count_marks(marks_list):
    fives_count = 0
    fours_count = 0
    triples_count = 0
    deuces_count = 0
    units_count = 0
    zeros_count = 0

    for element in marks_list:
        if element == 5:
            fives_count += 1
        elif element == 4:
            fours_count += 1
        elif element == 3:
            triples_count += 1
        elif element == 2:
            deuces_count += 1
        elif element == 1:
            units_count += 1
        elif element == 0:
            zeros_count += 1

    return fives_count, fours_count, triples_count, deuces_count, units_count, zeros_count


def count_fives_percentage(fives_count):
    fives_percentage = (fives_count * 100) / NUMBER_OF_MARKS
    return round(fives_percentage, 1)


def count_fours_percentage(fours_count):
    fours_percentage = (fours_count * 100) / NUMBER_OF_MARKS
    return round(fours_percentage, 1)


def count_triples_percentage(triples_count):
    triples_percentage = (triples_count * 100) / NUMBER_OF_MARKS
    return round(triples_percentage, 1)


def count_deuces_percentage(deuces_count):
    deuces_percentage = (deuces_count * 100) / NUMBER_OF_MARKS
    return round(deuces_percentage, 1)


def count_units_percentage(units_count):
    units_percentage = (units_count * 100) / NUMBER_OF_MARKS
    return round(units_percentage, 1)


def count_zeros_percentage(zeros_count):
    zeros_percentage = ((zeros_count * 100) / NUMBER_OF_MARKS)
    return round(zeros_percentage, 1)


def user_output(msg, marks_list):
    print("Exam Result Handling:")
    print(f"Marks: {marks_list}")
    print(msg)


def main():
    marks_list = create_list_of_marks()
    fives_count, fours_count, triples_count, deuces_count, units_count, zeros_count = count_marks(marks_list)
    fives_percentage = count_fives_percentage(fives_count)
    fours_percentage = count_fives_percentage(fours_count)
    triples_percentage = count_fives_percentage(triples_count)
    deuces_percentage = count_fives_percentage(deuces_count)
    units_percentage = count_fives_percentage(units_count)
    zeros_percentage = count_fives_percentage(zeros_count)
    msg = f"fives - {fives_percentage}% ({fives_count})\nfours - {fours_percentage}% ({fours_count})\n" \
          f"triples - {triples_percentage}% ({triples_count})\ndeuces - {deuces_percentage}% ({deuces_count})\n" \
          f"units - {units_percentage}% ({units_count})\nzeros - {zeros_percentage}% ({zeros_count})"
    user_output(msg, marks_list)


main()
