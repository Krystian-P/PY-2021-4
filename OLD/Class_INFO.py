class Card:
    def __init__(self, name, surname, company, number):
        self.name = name
        self.surname = surname
        self.company = company
        self.number = number

        # Variables
        self._label_lenght = 1

    @property
    def label_lenght(self):
        return len(self.name)+len(self.surname)


    def _contact(self):
        print(
            f"Kontaktujesz się z {self.name} {self.surname}, "
            f"{self.number}\n {self.label_lenght}")

    def contact(self):
        return self._contact()



person_1 = Card("Kate", "Grayer", "ABCO Food", "978-606-8889")
person_2 = Card("Mateusz", "Czarnecki", "Envirotecture Design Service", "79 572 58 45")
person_3 = Card("Seweryna", "Wysocka", "Hanover Shoe", "79 444 93 49")
person_4 = Card("Michał", "Wojciechowski", "Williams Bros.", "69 931 51 67")
person_5 = Card("Jaromir", "Tomaszewski", "Saturday Matinee", "78 849 35 27")


Card_Book = [person_1, person_2, person_3, person_4, person_5]



person_1.contact()


