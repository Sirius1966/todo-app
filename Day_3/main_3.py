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
        case 'exit':
            break
        case _:
            print("You entered an unknown command. Try again....")

print("Bye!")
