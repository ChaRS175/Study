import sys

class book: 
    def __init__(self,name,author,publication): #определение класса book
        self.name = name
        self.author = author
        self.publication = publication
        self.status = False
    
        
    def __str__(self):
        return f'Name: {self.name},Author: {self.author}, Year of publication: {self.publication}, Status: {self.status}' #красивый вывод всех значений класса
    

class library:
    def __init__(self): #определение класса library
        self.books = [] #задается массив(хранилище )

    def add_book(self,book_obj): #функция добавляющая книгу в библиотеку
        self.books.append(book_obj) # в массив библиотеки добавялется элемент книги

    def find_book(self, search_name):
        for b in self.books: # b — это конкретный объект книги из твоего списка
            if b.name == search_name: # Проверяем имя именно этой книги
                return b # Возвращаем найденный объект
        return None

    def borrow_book(self,search_name): #функция взятия книги
        book = self.find_book(search_name) #локальной переменной book задается значение из функции find_book
        if not book: #если такой книги нет, то возвращает то , что книга не найдена
            return 'Книга не найдена'
        elif book.status: #если статус объекта с классом book имеет значение True, то возвращает что ее нет в наличии
            return 'Книги нет в наличии'
        else: #меняет статус объекта с классом book на True если книга выдается успешно
            book.status = True
            return 'Книга выдана!'

    
    def all_books(self): # возвращает список всех книг находящихся в библиотеке
        names = []
        for book in self.books:
            names.append(book.name)
        return names




library1 = library() 



while True:
    choice_input = input('что вы хотите сделать? \n 1.добавить книгу \n 2.найти книгу \n 3.взять книгу \n 4.показать список всех книг \n 0.выйти \n ')

    if choice_input.isdigit(): # Проверяет, состоит ли строка только из цифр
        choice = int(choice_input)
    else:
        print("Ошибка: введите число от 0 до 4")
        continue # Возвращает в начало цикла while

    match choice:
        case 1:
            n = input('Название книги ')
            a = input('Автор книги ')
            y = input('год выпуска книг ')
            new_book = book(n,a,y)
            library1.add_book(new_book)
            print('книга добавлена!')
        case 2:
            name = input('Какую книгу вы ищете? ')
            result = library1.find_book(name)
            print(result if result else 'Книга не найдена :(')

        case 3:
            book_choice = input('Какую книгу вы хотите взять? ')
            print(library1.borrow_book(book_choice))
        case 4:
            print(library1.all_books())
        case 0:
            sys.exit(0)
        



            
            
