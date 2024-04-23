user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            # List-Comprehension:
            # new_todos = [item.strip('\n') for item in todos]
            # new_list = [new_item for item in old_list if condition]

            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index+1}.) {todo}")

        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            number = number - 1

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))

            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()

            removed_todo = todos.pop(number - 1).strip("\n")
            print(f"Todo '{removed_todo}' was successfully removed from the list!")

            with open("../files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

        # _ this underscore is per definition used as a variable for every any case or input
        case _:
            print("You entered an unknown command. Please try again....")

print("Bye!")
