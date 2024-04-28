import PySimpleGUI as Sg
from modules import zip as ze

Sg.theme("BlueMono")
# ------------------------------------------------------------
label1 = Sg.Text("Select zip file to extract: ")
input1 = Sg.Input(key="Input1")
choose_button1 = Sg.FileBrowse("Choose", key="zip_file")

label2 = Sg.Text("Select destination folder: ")
input2 = Sg.Input(key="Input2")
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")
exit_button = Sg.Button("Exit")
output_label = Sg.Text(key="output", text_color="green")
# -----------------------------------------------------------
window = Sg.Window("zip Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, exit_button, output_label],
                           ])
while True:
    event, values = window.read()
    print(event)
    print(values)
    # event output as a string: 'Extract'
    # values output as a dictionary:
    # {'Input1': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files/test1_zip.zip',
    # 'zip_file': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files/test1_zip.zip',
    # 'Input2': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files',
    # 'folder': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files'}
    match event:
        case "Extract":
            zip_file_path = values["zip_file"]
            folder = values["folder"]
            ze.extract_zip_file(zip_file_path, folder)
            window["output"].update(value="Extraction completed")
        case "Exit":
            break
        case Sg.WINDOW_CLOSED:
            break


window.close()
