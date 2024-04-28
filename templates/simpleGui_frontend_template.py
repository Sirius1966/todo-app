# ------------------------------------------------------------------------------
# 1. Imports
# ------------------------------------------------------------------------------
import PySimpleGUI as Sg

# -------------------------------------------------------------------------------
# 2. Theme of the widgets -> https://docs.pysimplegui.com/en/latest/documentation/module/themes/
# -------------------------------------------------------------------------------
Sg.theme("BlueMono")

# -------------------------------------------------------------------------------
# 3. Create widgets
# -------------------------------------------------------------------------------
label = Sg.Text("Text of Label")
input_box = Sg.InputText(tooltip="Tooltip Text", key="InputText identifier")
# issues about images as button:
# 1. size 2. Image is disappearing, when the mouse hovers over the image 3. tooltip
button = Sg.Button(image_source="../images/add.png",
                   size=5,
                   mouseover_colors="LightBlue2",
                   tooltip="Tooltip Text",
                   key="Button identifier")
list_box = Sg.Listbox(values=["List of values to show"],
                      key='Listbox identifier',
                      enable_events=True,
                      size=(45, 10))
# -----------------------------------------------------------------------------------------------
# 4. LAYOUT
# Creates a window object with the title 'Title of the app'
# layout=[[row1], [row2], ...] puts the label- and the input_box- widget inside the window
# -----------------------------------------------------------------------------------------------
window = Sg.Window('Title of the App',
                   layout=[[label],
                           [input_box],
                           [button, list_box]],
                   font=("Helvetica", 20))
# ------------------------------------------------------------------------------------------------
# 5. EVENT LOOP
# ------------------------------------------------------------------------------------------------
while True:
    # THE biggest deal method in the Window class! This is how you get all of your data from your Window.
    # Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds.
    # Will return timeout_key if no other GUI events happen first.

    # Params:
    # timeout – Milliseconds to wait until the Read will return IF no other GUI events happen first
    # timeout_key – The value that will be returned from the call if the timer expired
    # close – if True the window will be closed prior to returning
    # Returns:
    # (event, values)
    # event: str
    # values: dict: key=key of widget value=value of the widget
    event, values = window.read(timeout=200)

    print(1, "EVENT: ", event)  # -> str
    print(2, "VALUES: ", values)  # -> dictionary {key of widget: value of widget
    print(3, "INPUT BOX ITEMS: ", values["Listbox identifier"])

    match event:
        case "Event 1":
            window["key of event 1"].update(values="")

        case "Event 2":
            try:
                window["event 2"].update(values="")
            except IndexError:
                Sg.popup("information", font=("Helvetica", 20))

        case "Exit":
            break

        case Sg.WINDOW_CLOSED:
            break
# ----------------------------------------------------------------------------------------
# 6. CLOSE APP
# -----------------------------------------------------------------------------------------
window.close()
