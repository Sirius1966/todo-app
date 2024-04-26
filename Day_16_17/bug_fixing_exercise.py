import PySimpleGUI as Sg


def km_to_miles(kilometer):
    return kilometer / 1.6


label = Sg.Text("Kilometers: ")
input_box = Sg.InputText(tooltip="Enter todo", key="kms")
miles_button = Sg.Button("Convert")

output = Sg.Text(key="output")

window = Sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            km = int(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case Sg.WIN_CLOSED:
            break

window.close()
