from book import Book
from library import Library

lib = Library()
lib.add_book(Book("Тест", "Автор", 2020))
assert len(lib.show_books()) == 1, "Ошибка: книга не добавилась"

lib = Library()
lib.add_book(Book("Python", "Гвидо", 1991))
assert lib.borrow_book("Python") == True, "Ошибка: книга должна была выдаться"
assert lib.show_books()[0].status == "выдана", "Ошибка: статус должен быть 'выдана'"

assert lib.borrow_book("Python") == False, "Ошибка: нельзя выдать чужую выданную книгу"

assert lib.return_book("Python") == True, "Ошибка: книга должна успешно вернуться"
assert lib.show_books()[0].status == "доступна", "Ошибка: статус должен стать 'доступна'"

print('молодец')