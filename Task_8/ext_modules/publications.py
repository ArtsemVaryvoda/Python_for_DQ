import re
import sys
from datetime import datetime

class RecordGenerator:

    def create_header(self):
        class_name = self.__class__.__name__
        return f"{class_name} {(25 - len(class_name) - 1) * '-'}"


class News(RecordGenerator):
    def __str__(self):
        return self.record

    def __init__(self, news_text, city):
        super().__init__()
        self.news_text = news_text
        self.city_name = city
        self.publish_date = datetime.now().strftime("%Y/%m/%d %H.%M")
        self.record = self.create_header() + '\n' + self.news_text + '\n' + self.city_name + ', ' + self.publish_date


class PrivateAd(RecordGenerator):
    def __str__(self):
        return self.record

    def __init__(self, text, ad_valid_until):
        self.text = text
        self.ad_valid_until = ad_valid_until
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
            print(f'Incorrect dateformat {self.ad_valid_until} entered. Closing the program ')
            sys.exit()


class Congratulations(RecordGenerator):
    def __str__(self):
        return self.record

    def __init__(self, birthday_text, birthday_year):
        self.birthday_text = birthday_text
        self.birthday_year = birthday_year
        self.validate_birthday_year()
        self.record = self.create_header() + "\n" + self.birthday_text + "\n" \
                      + f"{self.__class__.__name__} with your {datetime.now().year - int(self.birthday_year)} birthday!" \
                      + "\n" + "Best Regards, your friend."

    def validate_birthday_year(self):
        pattern = re.compile('^\\d{4}$')
        if not pattern.match(self.birthday_year):
            print(f'Incorrect year {self.birthday_year} entered. Please, try again. Year should be in format 2000')
            sys.exit()
        else:
            if int(self.birthday_year) >= 2022:
                print("Looks like too early to celebrate :)")
                sys.exit()
            else:
                return self.birthday_year
