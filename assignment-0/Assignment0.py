""" Q1.
Write a Python Program to find out the last item in a
collection of 10 lists or 20 lists. Check if there are multiple
occurrences of these last items.
Input: Please take any .txt file of problem-1 of Assignment-1 and
consider 10 or 20 lines from the top."""

import csv
from collections import Counter


# reading the input file
def read_input_file(file_path, num_lines=100):

    with open("assignment-1\Q1input.txt", "r") as file:
        lines = file.readlines()
    return lines[:num_lines]


# Breaking the lines into words and storing the last word of each line
def process_lists(lines):
    last_items = []

    for line in lines:
        elements = line.strip().split()
        last_item = elements[-1]
        last_items.append(last_item)
    return last_items


# Counting the occurence of the last word
def count_last_elements(last_items):

    item_counts = Counter(last_items)

    return item_counts


# Main function
def main():
    file_path = "assignment-1\input_1.txt"
    num_lines = 20
    lines = read_input_file(file_path, num_lines)
    last_items = process_lists(lines)
    item_counts = count_last_elements(last_items)
    for item, count in item_counts.items():
        print(f"{item}")


if __name__ == "__main__":
    main()


"""Q2.
 Write a Python Program to check if there are repeated items
in a list. Consider this for 10 or 20 lists.
Input: Please take any .txt file of problem-1 of Assignment-1 and
consider 10 or 20 lines from the top."""

import csv
from collections import Counter


# reading the input file
def read_input_file(file_path, num_lines=100):

    with open("assignment-1\Q1input.txt", "r") as file:
        lines = file.readlines()
    return lines[:num_lines]


# Breaking the lines into words and storing the last word of each line
def process_lists(lines):
    last_items = []

    for line in lines:
        elements = line.strip().split()
        last_item = elements[-1]
        last_items.append(last_item)
    return last_items


# Counting the occurence of the last word
def count_last_elements(last_items):

    item_counts = Counter(last_items)

    return item_counts


# Counting the mutilple occurence of the last word
def multilple_occurence(item_counts):

    for item, count in item_counts.items():
        if count > 1:
            print(f"The last word '{item}' appears {count} times.")


# Main function
def main():
    file_path = "assignment-1\input_1.txt"
    num_lines = 20
    lines = read_input_file(file_path, num_lines)
    last_items = process_lists(lines)
    item_counts = count_last_elements(last_items)
    multilple_occurence(item_counts)


if __name__ == "__main__":
    main()

"""Q3.

Q3.
 Consider a table with multiple rows (let’s say 20 or 10) and a
single column. The entries in this column contain either 0 or
1. Write a Python Program to count the occurrences of 1 in
that single column.
Input: Take a single column and 20 rows of any one .xlsx from
problem-2 of Assignment-1."""

import pandas as pd
import openpyxl


def open_file1(file_path):
    df = pd.read_excel(file_path)
    return df


def count_occurence(df):
    count_one = 0
    for column in df.columns:
        for value in df[column]:
            if value == 1:
                count_one += 1
    return {"Count of 1:", count_one}


def main():
    file_path = "assignment-1/Q3sample.xlsx"
    df = open_file1(file_path)
    print(count_occurence(df))


if __name__ == "__main__":
    main()


"""Q4.
Consider a table with multiple rows (let’s say 20 or 10) and 10
single columns. The entries in these columns contain either
0 or 1. Write a Python Program to count the occurrences of 1
in all the columns.
Input: Take 10 columns and 20 rows of any one .xlsx from
problem-2 of Assignment-1."""


import pandas as pd
import openpyxl


def open_file2(file_path):
    df = pd.read_excel(file_path)
    return df


def count_occurence(df):
    count_zero = 0
    count_one = 0
    for column in df.columns:
        for value in df[column]:
            if value == 1:
                count_one += 1
            elif value == 0:
                count_zero += 1
    return {"Count of 1": count_one, "Count of 0": count_zero}


def main():
    file_path = "assignment-1/Q4sample.xlsx"
    df = open_file2(file_path)

    print(count_occurence(df))


if __name__ == "__main__":
    main()
