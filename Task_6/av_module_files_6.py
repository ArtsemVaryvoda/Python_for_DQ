import os
import sys
from ext_modules.file_data import FileData

default_path = 'C:\git\Python_for_DQ\Python_for_DQ\Task_6'
input_file_name = 'input_file.txt'


def choose_path():
    path = input('Type path of the file or just hit Enter to choose default path.'
                 ' Default path is C:\git\Python_for_DQ\Python_for_DQ\Task_6')
    if path == '':
        return default_path
    return path


def locate_file(file_path, file_name):
    try:
        with open(f'{file_path}\\{file_name}', "r+") as file:
            return file.read()
    except IOError:
        print(f'File {file_path}\\{file_name} was not found!')
        sys.exit()


def to_file(text):
    with open('News_feed.txt', 'a', encoding="utf-8") as f:
        f.write(text)
    print(text + 'Was added')


def delete_source_file():
    os.remove(input_file_name)


def main():
    file_path = choose_path()
    print(file_path)
    file_content = locate_file(file_path, input_file_name)
    file_data = FileData(file_content)
    to_file(str(file_data))
    delete_source_file()


main()
