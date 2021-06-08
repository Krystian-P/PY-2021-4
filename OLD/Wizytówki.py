from faker import Faker

faker = Faker()
card_list = []


class BaseContact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

        # Variables
        self._label_lenght = 1

    @property
    def label_lenght(self):
        return len(self.name)

    def contact(self):
        print(
            f"Wybieram numer {self.number} i dzwonie do {self.name} "
        )


class BusinessContact(BaseContact):
    def __init__(self, company, work_number, position, name, number, email):
        super().__init__(name, number, email)
        self.company = company
        self.work_number = work_number
        self.position = position

    def contact(self):
        print(
            f"Wybieram numer {self.work_number} i dzwonie do {self.name}"
        )
        # print(self.label_lenght)

def creat_contacts(class_selection, value):
    if class_selection == BaseContact:
        for Number in range(value):
            card_list.append(BaseContact(faker.name(), faker.phone_number(), faker.prefix()))
    elif class_selection == BusinessContact:
        for Number in range(value):
            card_list.append(
                BusinessContact(faker.company(), faker.phone_number(), faker.job(), faker.name(), faker.phone_number(),
                                faker.prefix()))
    else:
        print("Wrong class selection")


creat_contacts(BusinessContact, 2)
card_list[0].contact()
