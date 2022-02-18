import sys
from ext_modules.av_task_3_strings_refactored import normalize_string_case
from ext_modules.publications import News, PrivateAd, Congratulations
sys.path.append('/')


class FileData:
    def __str__(self):
        return self.text_to_append

    def __init__(self, data):
        self.file_content = data
        self.text_to_append = ''
        self.parce_file()

    @staticmethod
    def validate_record_type(record_type):
        if record_type not in ('News', 'Privatead', 'Congratulations'):
            print(f'Unsupported self type {record_type} in the file, exiting the program')
            sys.exit()

    @staticmethod
    def validate_elements_num(record_elements):
        if len(record_elements) != 3:
            print(f'{record_elements} should consists of 3 elements separated by |. Exiting.')
            sys.exit()

    @staticmethod
    def normalize_list(record_elements):
        for i in range(len(record_elements)):
            record_elements[i] = normalize_string_case(record_elements[i])
        return record_elements

    @staticmethod
    def add_empty_rows_below(text):
        return text + '\n' + '\n'

    def parce_file(self):
        for row in self.file_content.split('\n'):
            record_elements = self.normalize_list(row.split(' | '))
            self.validate_elements_num(record_elements)
            self.validate_record_type(record_elements[0])
            if record_elements[0] == 'News':
                obj = News(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Privatead':
                obj = PrivateAd(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
            elif record_elements[0] == 'Congratulations':
                obj = Congratulations(record_elements[1], record_elements[2])
                self.text_to_append += self.add_empty_rows_below(str(obj))
