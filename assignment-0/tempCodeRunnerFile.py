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
