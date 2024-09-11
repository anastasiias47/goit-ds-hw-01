from entity import Name, Phone, Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phones_to_add: str):
        self.phones.append(Phone(phones_to_add))

    def remove_phone(self, phone_to_remove: str):
        self.phones.remove(Phone(phone_to_remove))

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in map(lambda phone: phone.value, self.phones):
            raise ValueError('No such number for this person')
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone_to_find):
        if phone_to_find in map(lambda phone: phone.value, self.phones):
            return Phone(phone_to_find)
        else:
            return None

    def add_birthday(self, birthday_to_add):
        self.birthday = Birthday(birthday_to_add)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"

