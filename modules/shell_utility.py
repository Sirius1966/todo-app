import shutil


def make_zip_file(name_outputfile: str, out_of_files: str):
    """
    It creates a 'name_outputfile' with .zip Suffix from all the files in the 'out_of_files'
    directory.
    :param: name_outputfile: str: e.g. 'output'
    :param: out_of_files: str: 'files' directory
    :return: None
    """
    shutil.make_archive(name_outputfile, "zip", out_of_files)


if __name__ == "__main__":
    make_zip_file("output", '../files')
