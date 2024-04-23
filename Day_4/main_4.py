user_prompt = "Type 'add', 'show', 'edit' or 'exit': "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter the number of the todo to edit: "))
            list_number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[list_number] = new_todo
        case 'exit':
            break
        case _:
            print("You entered an unknown command. Try again....")

print("Bye!")
