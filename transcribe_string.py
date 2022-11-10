#!/usr/bin/env python
import re

INPUT = """Patient presents today with several issues. Number one BMI has increased by 10%
since their last visit number next patient reports experiencing dizziness several times
in the last two weeks. Number next patient has a persistent cough that hasn’t
improved for last 4 weeks Number next patient is taking drug number five several
times a week"""


class UnknownNumber(Exception):
    pass


def word_to_num(word: str):
    match word.lower():
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            raise UnknownNumber


def main():
    splits_on_number_next = re.split("number next", INPUT, flags=re.IGNORECASE)

    starting_item_regex = r"number\s\w+"

    # matches "number one" in sample input, then split on the space, and grab the second item (ex. "one")
    first_num_str = re.search(starting_item_regex, splits_on_number_next[0], flags=re.IGNORECASE).group().split(' ')[1]
    starting_number = word_to_num(first_num_str)

    intro_and_start_item = re.split(starting_item_regex, splits_on_number_next[0], maxsplit=1, flags=re.IGNORECASE)

    output = list()

    output.append(intro_and_start_item[0].strip().replace('\n', ' '))  # add intro

    start_item = intro_and_start_item[1].strip().replace('\n', ' ')  # clean up any newlines in middle of string
    output.append(f"{starting_number}. {start_item}")  # add start item with corresponding number

    starting_number += 1  # increment the number for the next item in the list
    for item in splits_on_number_next[1:]:
        item = item.strip().replace('\n', ' ').capitalize()  # clean up any newlines in middle of string and capitalize first letter
        output.append(f'{starting_number}. {item}')
        starting_number += 1

    return '\n'.join(output)  # output the list as a string with newlines between each item


if __name__ == "__main__":
    output = main()
    print(output)


def test_main():
    expected_output = """Patient presents today with several issues.
1. BMI has increased by 10% since their last visit
2. Patient reports experiencing dizziness several times in the last two weeks.
3. Patient has a persistent cough that hasn’t improved for last 4 weeks
4. Patient is taking drug number five several times a week"""

    actual_output = main()
    assert actual_output == expected_output