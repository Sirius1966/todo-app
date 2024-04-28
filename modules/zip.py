import pathlib
import zipfile


def make_zip_file(filepaths: list, dest_dir: str, name_of_file: str):
    """
    Make a zip file from the files with the filepaths in the list and is stored in the dest_dir
    with the name_of_file. The name of the file must have the suffix .zip. The pathlib Library
    concatenates the dest_dir and the name_of_file to the dest_path, which is needed for the
    zipfile library.
    :param filepaths: list: e.g. ["../files/todos.txt", "../files/weather.csv"]
    :param dest_dir: str: e.g. "../files"
    :param name_of_file: str: e.g. "compress.zip"
    :return: None
    """
    dest_path = pathlib.Path(dest_dir, name_of_file)
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            # filepath -> e.g. '/Users/michaeldr.hegner/Documents/Python/3_txt_files/City_List.txt'
            filepath = pathlib.Path(filepath)
            # filepath.name -> e.g. 'City_List.txt'
            archive.write(filepath, arcname=filepath.name)


def extract_zip_file(zip_file_path: str, dest_dir: str):
    """
    It will extract the zip file and put the extracted files to the destination folder
    :param zip_file_path: str: absolute path to the zip file as a string
    :param dest_dir: str: destination folder's absolute path as a string
    :return: None
    """
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall(dest_dir)


if __name__ == "__main__":
    extract_zip_file("/Users/michaeldr.hegner/PycharmProjects/Udemy_Python_in_60_days/files/compressed.zip",
                     '/Users/michaeldr.hegner/PycharmProjects/Udemy_Python_in_60_days/files')
    # make_zip_file(filepaths=["../files/todos.txt", "../files/weather.csv"],
    #             dest_dir="../files",
    #              name_of_file="compress.zip")

