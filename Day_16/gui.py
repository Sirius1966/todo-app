import PySimpleGUI as sg
from modules import functions

# Create widgets
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# Creates a window object with the title 'My To-Do App'
# layout=[[row1], [row2], ...] puts the label- and the input_box- widget inside the window
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    # ('Add', {'to_do': 'hi'}) event = 'Add' values = {'to_do': 'hi'}
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
