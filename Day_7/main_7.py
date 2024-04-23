user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

# Ich würde diesen Abschnitt an den Anfang setzen
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            f = open("../files/todos.txt", 'w')
            f.writelines(todos)
            f.close()

        case 'show' | 'display':
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]
            # new_list = [new_item for item in old_list if condition]

            for index, todo in enumerate(todos):
                todo = todo.strip('\n')
                print(f"{index+1}.) {todo}")

        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            list_number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[list_number] = new_todo

        case 'complete':
            number = int(input("Enter the number of the todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break

        case _:
            print("You entered an unknown command. Try again....")

print("Bye!")
