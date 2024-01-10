# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
# - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        else:
            raise ValueError("Can only add two Rectangle instances")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            return self.area() - other.area()
        else:
            raise ValueError("Can only subtract two Rectangle instances")

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Rectangle):
            return self.area() != other.area()
        else:
            return True

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise ValueError("Can only compare two Rectangle instances")

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            raise ValueError("Can only compare two Rectangle instances")

    def __len__(self):
        return self.x + self.y


#
#     створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.shoe_size == self.shoe_size:
                return cinderella
        return None

class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    @classmethod
    def get_count(cls):
        return cls.count



    # 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
    # 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
    # 3) Створити клас Main в якому буде:
    # - змінна класу printable_list яка буде зберігати книжки та журнали
    #                                                            - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
    #                                                                                                                                                                                                                         - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
    #                                                                                                                                                                                                                                                                                                                       - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
    #
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()

# Example usage
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()