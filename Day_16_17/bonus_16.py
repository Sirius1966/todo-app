import PySimpleGUI as Sg
from modules import zip as zc


label1 = Sg.Text("Select Files to compress: ")
input1 = Sg.Input(key="Input1")
choose_button1 = Sg.FilesBrowse("Choose", key="files")

label2 = Sg.Text("Select destination folder: ")
input2 = Sg.Input(key="Input2")
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

compress_button = Sg.Button("Compress")
output_label = Sg.Text(key="output", text_color="green")

window = Sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label],
                           ])
while True:
    event, values = window.read()
    print(event)
    # values output:
    # {'Input1': '/Users/michaeldr.hegner/Documents/Python/3_txt_files/date_source.txt;
    # /Users/michaeldr.hegner/Documents/Python/3_txt_files/clients.txt',
    # 'files': '/Users/michaeldr.hegner/Documents/Python/3_txt_files/date_source.txt;
    # /Users/michaeldr.hegner/Documents/Python/3_txt_files/clients.txt',
    # 'Input2': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files',
    # 'folder': '/Users/michaeldr.hegner/Documents/Python/4_compressed_files'}
    print(values)
    filepaths = values["files"].split(";")  # -> list
    folder = values["folder"]  # -> str
    zc.make_zip_file(filepaths, folder, "test1_zip.zip")
    window["output"].update(value="Compression completed")


window.close()
