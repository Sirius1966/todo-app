from modules import functions
import time

user_prompt = "Type 'add', 'show', 'edit', 'complete' or 'exit': "

now = time.strftime("%d.%b.%Y %H:%M:%S")
print("It is ", now)

while True:
    # Get user input and strip space chars from it
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

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

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not an valid integer. Try again...")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos.pop(number - 1).strip("\n")
            print(f"Todo '{removed_todo}' was successfully removed from the list!")

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number. Try again...")
            continue

    elif user_action.startswith("exit"):
        break

    # _ this underscore is per definition used as a variable for every any case or input
    else:
        print("You entered an unknown command. Please try again....")

print("Bye!")
