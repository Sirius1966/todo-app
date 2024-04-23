def get_todos(filepath: str) -> list:
    """
    Gets the todo_items from the textfile in the files directory
    :return: todos_local:list[str]
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath: str, todos_arg: list):
    """
    writes the todos list in the textfile with the filepath
    :param filepath: str: textfile directory
    :param todos_arg: list: list of todos
    :return: None
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("../files/todos.txt")

        todos.append(todo + '\n')

        write_todos("../files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("../files/todos.txt")

        # List-Comprehension:
        # new_todos = [item.strip('\n') for item in todos]
        # new_list = [new_item for item in old_list if condition]

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index+1}.) {todo}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("../files/todos.txt")

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("../files/todos.txt", todos)
        except ValueError:
            print("Your command is not an valid integer. Try again...")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("../files/todos.txt")

            removed_todo = todos.pop(number - 1).strip("\n")
            print(f"Todo '{removed_todo}' was successfully removed from the list!")

            write_todos("../files/todos.txt", todos)
        except IndexError:
            print("There is no item with that number. Try again...")
            continue

    elif user_action.startswith("exit"):
        break

    # _ this underscore is per definition used as a variable for every any case or input
    else:
        print("You entered an unknown command. Please try again....")

print("Bye!")
