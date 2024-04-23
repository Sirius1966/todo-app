import csv


def get_csv(filename: str) -> list:
    """
    Get csv data from a file with filename and gives the data back as a list. Each element of the list
    represents a row of the table. The header for table is mentioned in the first element of the list.
    :param filename:str: e.g. "weather.csv"
    :return: data: list: e.g. [['stations', 'temperatures'], ['New York', '20'], ['Lübbecke', '23']]
    """
    with open(f"../files/{filename}", "r") as file:
        data = list(csv.reader(file))
    return data


def extract_data(search_item: str, search_column: str, csv_data: list) -> str:
    """
    Extract data from csv_data list: Looks for the interested column datas (search_column: str)
    and extracts the value in the search_column for search_item: str in the same row and returns
    it as 'item'. So it is a cross finding: The row with the search_item and the column in the
    search_column.
    If the search_item is not found,then it will return a string 'False'.

    :param search_item: str: value of a list: e.g.'New York
    :param search_column: str: 'temperatures'
    :param csv_data: list: e.g. [['stations', 'temperatures'], ['New York', '20'], ['Lübbecke', '23']]
    :return: item: str: e.g. '20'
    """

    header = csv_data[0]
    index = header.index(search_column)
    for row in csv_data:
        if search_item in row:
            item = row[index]
            return item
        else:
            continue

    return 'False'


if __name__ == "__main__":
    weather_data = get_csv("weather.csv")
    search = extract_data("New York", "temperatures", weather_data)
    print(search)
