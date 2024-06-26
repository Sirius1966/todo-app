import PySimpleGUI as Sg
from modules import functions

# Create widgets
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))
edit_button = Sg.Button("Edit")

# Creates a window object with the title 'My To-Do App'
# layout=[[row1], [row2], ...] puts the label- and the input_box- widget inside the window
window = Sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    # ('Add', {'to_do': 'hi'}) event = 'Add' values = {'to_do': 'hi'}
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"].replace("\n", "") + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WINDOW_CLOSED:
            break

window.close()
