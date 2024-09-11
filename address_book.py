from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None

    def delete(self, name):
        del self.data[name]

    @staticmethod
    def string_to_date(date_string):
        return datetime.strptime(date_string, "%d.%m.%Y")

    @staticmethod
    def date_to_string(date):
        return datetime.strftime(date, "%d.%m.%Y")

    @staticmethod
    def prepare_user_list(user_data):
        prepared_list = []
        for key in user_data.keys():
            prepared_list.append({"name": key, "birthday": user_data[key].birthday.value})
        return prepared_list

    @staticmethod
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    @staticmethod
    def adjust_for_weekend(birthday):
        if birthday.weekday() >= 5:
            return AddressBook.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days = 7):
        upcoming_birthdays = []
        today = datetime.today()

        for user in AddressBook.prepare_user_list(self.data):
            birthday_this_year = user["birthday"].replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year + timedelta(days=366)

            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = AddressBook.adjust_for_weekend(birthday_this_year)

                congratulation_date_str = AddressBook.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

            return upcoming_birthdays

    def __str__(self):
        output_string = ""
        for key in self.data.keys():
            output_string += f"{key}: Phones ({'; '.join(p.value for p in self.data[key].phones)}), Birthday {self.data[key].birthday}\n"

        return output_string




