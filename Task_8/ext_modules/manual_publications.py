import re
import sys
from datetime import datetime


def main():
    user_choice = input(
        "n to add News\np to add PrivateAd\nc to Congratulate someone with birthday.\n Any other input - exit\n")
    if 'n' == user_choice:
        News().to_file()
    elif 'p' == user_choice:
        PrivateAd().to_file()
    elif 'c' == user_choice:
        Congratulations().to_file()
    else:
        print('Good luck! See ya next time')


if __name__ == "__main__":
    main()


class RecordGeneratorManual:
    def __init__(self):
        self.text = input(f"Please, enter {self.__class__.__name__} message text: ")

    def to_file(self):
        with open('News_feed.txt', 'a', encoding="utf-8") as f:
            f.write(self.record + '\n' + '\n')
        print(self.record + '\n' + 'Was added')

    def create_header(self):
        class_name = self.__class__.__name__
        return f"{class_name} {(25 - len(class_name) - 1) * '-'}"


class News(RecordGeneratorManual):
    def __init__(self):
        super().__init__()
        self.city_name = input("Please, enter name of the city: ")
        self.publish_date = datetime.now().strftime("%Y/%m/%d %H.%M")
        self.record = self.create_header() + '\n' + self.text + '\n' + self.city_name + ', ' + self.publish_date


class PrivateAd(RecordGeneratorManual):
    def __init__(self):
        super().__init__()
        self.ad_valid_until \
            = input("Please, enter date until which ad will be actual in format 2021/12/31. Separated by / ")
        self.get_ad_validness_date()
        self.current_date = datetime.now()
        dates_diff = self.ad_valid_until - self.current_date
        if dates_diff.days < 0:
            print(f"Looks like ad expired. Exiting the program")
            sys.exit()
        self.record = self.create_header() + '\n' + self.text + '\n' \
                      + f'Actual until: ' + str(self.ad_valid_until.strftime('%Y/%m/%d')) \
                      + f' {dates_diff.days} days left'

    def get_ad_validness_date(self):
        try:
            self.ad_valid_until = datetime.strptime(self.ad_valid_until, '%Y/%m/%d')
        except ValueError as e:
            self.ad_valid_until = input('Incorrect format entered. Please, try again. Enter exit to close the program ')
            if "exit" != self.ad_valid_until:
                self.get_ad_validness_date()
            else:
                sys.exit()


class Congratulations(RecordGeneratorManual):
    def __init__(self):
        super().__init__()
        self.congratulator_name = input('Please, enter your name: ')
        self.birthday_year = input('When birthday boy/girl was born? ')
        self.validate_birthday_year()
        self.record = self.create_header() + "\n" + self.text + "\n" \
                      + f"{self.__class__.__name__} with your {datetime.now().year - int(self.birthday_year)} birthday!" \
                      + "\n" f"Best Regards, {self.congratulator_name}"

    def validate_birthday_year(self):
        pattern = re.compile('\d{4}')
        if pattern.match(self.birthday_year):
            if int(self.birthday_year) >= 2022:
                print("Looks like too early to celebrate :)")
                sys.exit()
            else:
                return self.birthday_year
        else:
            self.birthday_year = input('Incorrect year enter. Please, try again. Year should be in format 2000')
            if self.birthday_year != "exit":
                self.validate_birthday_year()
            else:
                sys.exit()
