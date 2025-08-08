class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, book_name, author, pages_count, isbn, is_reserved):
        self.book_name = book_name
        self.author = author
        self.pages_count = pages_count
        self.isbn = isbn
        self.is_reserved = is_reserved

    def printout_book(self):
        if self.is_reserved:
            print(f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_count},'
                  f' материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_count},'
                  f' материал: {self.page_material}')


class Schoolbook(Book):
    def __init__(self, book_name, author, pages_count, isbn, is_reserved, school_subject, class_number, has_tasks):
        super().__init__(book_name, author, pages_count, isbn, is_reserved)
        self.school_subject = school_subject
        self.class_number = class_number
        self.has_tasks = has_tasks

    def printout_schoolbook(self):
        if self.is_reserved:
            print(f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_count}, '
                  f'Предмет: {self.school_subject}, Класс: {self.class_number}, Зарезервирован')
        else:
            print(f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_count}, '
                  f'Предмет: {self.school_subject}, Класс: {self.class_number}')


books = [
    Book('Война и мир, 1 том', 'Л.Н. Толстой', 422, '978-5-9268-4217-1', False),
    Book('Война и мир, 2 том', 'Л.Н. Толстой', 466, '978-5-9268-4217-2', False),
    Book('Война и мир, 3 том', 'Л.Н. Толстой', 448, '978-5-9268-4217-3', False),
    Book('Война и мир, 4 том', 'Л.Н. Толстой', 458, '978-5-9268-4217-4', False),
    Book('Анна Каренина', 'Л.Н. Толстой', 310, '978-5-9268-4217-5', True)
]

schoolbooks = [
    Schoolbook('Алгебра', 'Иванов', 200, '978-5-9268-4232-3', True, 'Математика', 9, True),
    Schoolbook('История России', 'Петров', 150, '978-5-9244-4217-0', False, 'История', 8, True),
    Schoolbook('Физика', 'Пёрышкин', 250, '922-5-9244-4278-1', False, 'Физика', 7, True)
]

for book in books:
    book.printout_book()

for book in schoolbooks:
    book.printout_schoolbook()
