import glob


def get_filepaths(files: str) -> list:
    """
    Get all files from the 'files' directory with a special suffix e.g. '*.txt'
    and returns them as a list.
    :param files: str: e.g.'*.txt'
    :return: myfiles: list: e.g. ['../files/todos.txt']
    """
    myfiles = glob.glob(f"../files/{files}")
    return myfiles


def get_contents(filepaths: list) -> dict:
    """
    Get content of each filepath in filepaths from 'get_filepaths' and returns it as a dictionary.
    :param filepaths: list: e.g. ['../files/todos.txt']
    :return: contents: dict: e.g. {'../files/todos.txt': 'clean the basket\nfly to germany\nclean the code\n'}
    """
    contents = {}
    for filepath in filepaths:
        with open(filepath, "r") as file:
            content = file.read()
            contents[filepath] = content
    return contents


if __name__ == "__main__":
    my_files = get_filepaths("*.txt")
    print(my_files)
    my_contents = get_contents(my_files)
    print(my_contents)
