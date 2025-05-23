import pandas as pd


def read_input_file(file_path):
    df = pd.read_csv(file_path)
    return df


def process_lists(lines):
    first_items = []
    last_items = []

    for line in lines:
        element = line.strip().split()
        first_items.append(element[0])
        last_items.append(element[-1])
    return first_items, last_items
    # for index, row in df.iterrows():
    #     first_items.append(row.iloc[0])
    #     last_items.append(row.iloc[-1])
    # return first_items, last_items
    # first_items = df.iloc[:, 0].tolist()
    # last_items = df.iloc[:, -1].tolist()
    # return first_items, last_items


def main(file_path):

    df = read_input_file(file_path)
    lines = read_input_file(file_path)
    first_items, last_items = process_lists(lines)
    print("First items:", first_items)
    print("Last items:", last_items)


if __name__ == "__main__":
    file_path = "assignment-1/input_1.txt"
    main(file_path)
