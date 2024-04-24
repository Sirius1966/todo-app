import PySimpleGUI as sg
from modules import functions

# Create widgets
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# Creates a window object with the title 'My To-Do App'
# layout=[[row1], [row2], ...] puts the label- and the input_box- widget inside the window
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
