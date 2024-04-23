user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("../files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

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

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not an valid integer. Try again...")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            removed_todo = todos.pop(number - 1).strip("\n")
            print(f"Todo '{removed_todo}' was successfully removed from the list!")

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("There is no item with that number. Try again...")
            continue

    elif user_action.startswith("exit"):
        break

    # _ this underscore is per definition used as a variable for every any case or input
    else:
        print("You entered an unknown command. Please try again....")

print("Bye!")
