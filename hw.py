# Задание №1-----------------------------------------------------------------------------------------------------------------------------------------



class Car:
    def __init__(self):
        pass

    def input_data(self):
        self.name = input("Введите название модели: ")
        self.__year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.__engine_capacity = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.cost = input("Введите цену: ")
    
    def get_year(self):
        return self.__year
    
    def get_engine_capacity(self):
        return self.__engine_capacity
    


    def output_data(self):
        return (self.name, self.get_year(), self.manufacturer, self.get_engine_capacity(), self.color, self.cost)

toyota= Car()
print(toyota.input_data())
print(toyota.output_data())







# Задание №2-----------------------------------------------------------------------------------------------------------------------------------------


class Book:
    def __init__(self):
        pass

    def input_data(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher  = input("Введите издателя: ")
        self.__genre = input("Введите жанр: ")
        self.__author = input("Введите автора: ")
        self.cost = int(input("Введите цену: "))
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    


    def output_data(self):
        return (self.name, self.year, self.publisher, self.get_genre(), self.get_author(), self.cost)

book= Book()
print(book.input_data())
print(book.output_data())







# Задание №3-----------------------------------------------------------------------------------------------------------------------------------------



class Stadium:
    def __init__(self):
        pass

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.__date = input("Введите дату открытия: ")
        self.country  = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.__capacity = input("Введите вместимость: ")
    
    def get_capacity(self):
        return self.__capacity
    
    def get_date(self):
        return self.__date
    


    def output_data(self):
        return (self.name, self.get_date(), self.country, self.city, self.get_capacity())

stadium= Stadium()
print(stadium.input_data())
print(stadium.output_data())







