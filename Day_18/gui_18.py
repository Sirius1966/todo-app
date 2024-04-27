# Imports
import PySimpleGUI as Sg
import time
from modules import functions

# Theme of the widgets
Sg.theme("BlueMono")

# Create widgets
clock = Sg.Text("", key="clock")
label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

# Creates a window object with the title 'My To-Do App'
# layout=[[row1], [row2], ...] puts the label- and the input_box- widget inside the window
window = Sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    # ('Add', {'to_do': 'hi'}) event = 'Add' values = {'to_do': 'hi'}
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d.%b.%Y %H:%M:%S"))
    # print(1, "EVENT: ", event)
    # print(2, "VALUES: ", values)
    # print(3, "INPUT BOX ITEMS: ", values["todos"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].replace("\n", "") + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                Sg.popup("Please Select an item first", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup("Please Select an item first", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WINDOW_CLOSED:
            break

window.close()
