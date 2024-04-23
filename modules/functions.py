FILEPATH = "../files/todos.txt"


def get_todos(filepath=FILEPATH) -> list:
    """
    Gets the todo_items from the textfile in the files directory
    and returns a list of todo_items.
    :return: todos_local:list[str]
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg: list, filepath=FILEPATH):
    """
    writes the todos list in the textfile with the filepath
    :param filepath: str: textfile directory
    :param todos_arg: list: list of todos
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")