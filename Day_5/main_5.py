user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for index, todo in enumerate(todos):
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
