import random
from faker import Faker

fake = Faker()

library = []
get_list = []


class Movie:
    def __init__(self, title, production_year, movie_genre, play_amount):
        self.title = title
        self.production_year = production_year
        self.movie_genre = movie_genre
        self.play_amount = play_amount

    def play(self):
        self.play_amount += 1

    def info(self):
        print(f"{self.title} ({self.production_year})")

    def __repr__(self):
        return f"Film = {self.title}, rok produkcji = {self.production_year}, gatunek = {self.movie_genre}, liczba odtworzeń = {self.play_amount}"


class Series(Movie):
    def __init__(self, chapter_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapter_number = chapter_number
        self.season_number = season_number

    def info(self):
        if self.season_number < 10 <= self.chapter_number:
            print(f"{self.title} S0{self.season_number}E{self.chapter_number}")
        elif self.chapter_number < 10 <= self.season_number:
            print(f"{self.title} S{self.season_number}E0{self.chapter_number}")
        elif self.season_number < 10 and self.chapter_number < 10:
            print(f"{self.title} S0{self.season_number}E0{self.chapter_number}")
        else:
            print(f"{self.title} S0{self.season_number}E{self.chapter_number}")

    def play(self):
        self.play_amount += 1

    def __repr__(self):
        return f"Serial = {self.title}, rok produkcji = {self.production_year}, gatunek = {self.movie_genre}, liczba " \
               f"odtworzeń = {self.play_amount}, luiczba odcinków = {self.chapter_number}, numer " \
               f"sezonu={self.season_number} "


M1 = Movie(fake.name(), random.randrange(1000, 2021), fake.name(), random.randrange(0, 120000))
M2 = Series(random.randrange(1, 40), random.randrange(1, 10), fake.name(), random.randrange(1000, 2021), fake.name(),
            random.randrange(0, 120000))
M3 = Movie(fake.name(), random.randrange(1000, 2021), fake.name(), random.randrange(0, 120000))
M4 = Series(random.randrange(1, 40), random.randrange(1, 10), fake.name(), random.randrange(1000, 2021), fake.name(),
            random.randrange(0, 120000))
M5 = Movie(fake.name(), random.randrange(1000, 2021), fake.name(), random.randrange(0, 120000))
library.append(M1)
library.append(M2)
library.append(M3)
library.append(M4)
library.append(M5)


def list_creator():
    choice = int(input("1.Film \n2.Serial\n Co chcesz dodać do listy (wybierz 1 lub 2): "))
    if choice == 1:
        object = Movie(input("Podaj tytuł: "), input("Podaj rok produkcji: "), input("Podaj kategorie: "),
                       int(input("Podaj liczbę odtworzeń: ")))
        library.append(object)
    elif choice == 2:
        object = Series(input("Podaj numer odcinka: "), input("Podaj numer serialu: "), input("Podaj tytuł: "),
                        input("Podaj rok produkcji: "), input("Podaj kategorie: "),
                        int(input("Podaj liczbę odtworzeń: ")))
        library.append(object)
    else:
        print("Nie poprawny wybór!")


def sort_lib_title(lib):
    return lib.title


def get_movie():
    for position in library:
        if position.__class__ == Movie:
            get_list.append(position)
    get_list_title = sorted(get_list, key=sort_lib_title)
    for length in range(0, len(get_list_title)):
        print(get_list_title[length])


def get_series():
    for position in library:
        if position.__class__ == Series:
            get_list.append(position)
    get_list_title = sorted(get_list, key=sort_lib_title)
    for length in range(0, len(get_list_title)):
        print(get_list_title[length])


def search():
    looking_for = input("Podaj szukany tytuł:")
    for count, value in enumerate(library):
        if value.title == looking_for:
            print(f"Numer w bibliotece filmu/serialu pt. '{value.title}', to:{count}")


def generate_view():
    value = random.randrange(1, 101)
    library[random.randrange(0, len(library))].play_amount = library[
                                                                 random.randrange(0, len(library))].play_amount + value


def multi_generate_views():
    for value in range(0, 10):
        generate_view()


def myFunc(e):
    return len(e)


def sort_lib_view(lib):
    return lib.play_amount


def top_titles(count):  # do tej funkcji można by wykorzystać funkcje get_movie, get_series/ do zrobienia
    # w wolnej chwili
    content_type = input("Czego szukasz (film/serial):")
    if content_type == "film":
        for position in library:
            if position.__class__ == Movie:
                get_list.append(position)
        get_list_title = sorted(get_list, key=sort_lib_view, reverse=True)
        for length in range(0, count):
            print(get_list_title[length])
    if content_type == "serial":
        for position in library:
            if position.__class__ == Movie:
                get_list.append(position)
        get_list_title = sorted(get_list, key=sort_lib_view, reverse=True)
        for length in range(0, count):
            print(get_list_title[length])


top_titles(2)
