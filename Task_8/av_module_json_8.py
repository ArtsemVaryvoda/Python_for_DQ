import json
import os
import sys
from ext_modules.manual_publications import main as start_manual_load
from ext_modules.file_data import FileData
from ext_modules.csv_stat import CSVStat

default_path = 'C:\git\Python_for_DQ\Python_for_DQ\Task_8'
input_file_name = 'input_file.txt'
news_feed = 'News_feed.txt'
json_name = 'input.json'


def json_to_list(path, file):
    with open(f'{path}\\{file}') as json_file:
        json_list = json.load(json_file)
    return json_list


def choose_path():
    path = input(f'Type path of the file or just hit Enter to choose default path.'
                 ' Default path is C:\git\Python_for_DQ\Python_for_DQ\Task_8 \n')
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
    with open(news_feed, 'a', encoding="utf-8") as f:
        f.write(text)
    print(text + 'Was added')


def delete_source_file():
    os.remove(input_file_name)


def main():
    file_path = choose_path()
    user_choice = input("m for manual, f for .txt file, j for json. Any other input - exit\n")
    if user_choice == 'm':
        start_manual_load()
    elif user_choice == 'f':
        file_content = locate_file(file_path, input_file_name)
        file_data = FileData(file_content, 'f')
        to_file(str(file_data))
        #delete_source_file()
    elif user_choice == 'j':
        json_list = json_to_list(file_path, json_name)
        file_data = FileData(json_list, 'j')
        to_file(str(file_data))
    else:
        print('Good luck!')
        sys.exit()
    CSVStat(file_path, news_feed)


main()
