# from book import Book
# from library import Library
#
#
# def main():
#     library = Library()
#
#     library.add_book(Book("Война и мир", "Л. Толстой", 1869))
#     library.add_book(Book("1984", "Дж. Оруэлл", 1949))
#
#     while True:
#         print("\n===== МОЯ БИБЛИОТЕКА =====")
#         print("1. Добавить книгу")
#         print("2. Показать все книги")
#         print("3. Взять книгу")
#         print("4. Вернуть книгу")
#         print("5. Выход")
#
#         choice = input("Выберите пункт меню (1-5): ").strip()
#
#         if choice == "1":
#             title = input("Введите название книги: ")
#             author = input("Введите автора: ")
#             try:
#                 year = int(input("Введите год выпуска: "))
#                 new_book = Book(title, author, year)
#                 library.add_book(new_book)
#                 print("✅ Книга успешно добавлена!")
#             except ValueError:
#                 print("❌ Год должен быть числом!")
#
#         elif choice == "2":
#             books = library.show_books()
#             if not books:
#                 print("Библиотека пуста.")
#             else:
#                 print("\nСписок книг:")
#                 i = 1
#                 for book in books:
#                     print(f"{i}. {book}")
#                     i += 1
#
#         elif choice == "3":
#             title = input("Введите название книги, которую хотите взять: ")
#             result = library.borrow_book(title)
#             if result is True:
#                 print("✅ Вы успешно взяли книгу.")
#             elif result is False:
#                 print("⚠️ Эта книга уже выдана!")
#             else:
#                 print("❌ Книга не найдена.")
#
#         elif choice == "4":
#             title = input("Введите название книги для возврата: ")
#             result = library.return_book(title)
#             if result is True:
#                 print("✅ Книга успешно возвращена.")
#             elif result is False:
#                 print("⚠️ Эта книга не числилась выданной.")
#             else:
#                 print("❌ Книга не найдена.")
#
#         elif choice == "5":
#             print("До свидания!")
#             break
#         else:
#             print("❌ Неверный выбор, введите число от 1 до 5.")
#
#
# if __name__ == "__main__":
#     main()

from book import Book
from library import Library

def main():
    library = Library()

    library.add_book(Book("Война и мир", "Л. Толстой", 1869))
    library.add_book(Book("1984", "Дж. Оруэлл", 1949))

    while True:
        print("\033[35m===== МОЯ БИБЛИОТЕКА =====")
        print("\033[36m1. Добавить книгу")
        print("\033[36m2. Показать все книги")
        print("\033[36m3. Взять книгу")
        print("\033[36m4. Вернуть книгу")
        print("\033[36m5. Выход")

        choice = input("\033[32mВыберите пункт меню (1-5): ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            try:
                year = int(input("Введите год выпуска: "))
                new_book = Book(title, author, year)
                library.add_book(new_book)
                print("\033[32m Книга успешно добавлена!")
            except ValueError:
                print("\033[31m Ошибка: год должен быть числом!")

        elif choice == "2":
            books = library.show_books()
            if not books:
                print("\033[31mБиблиотека пуста.")
            else:
                print("\nСписок книг:")
                i = 1
                for book in books:
                    print(f"{i}. {book}")
                    i += 1

        elif choice == "3":
            title = input("Введите название книги, которую хотите взять: ")
            result = library.borrow_book(title)
            if result is True:
                print("\033[32m Вы успешно взяли книгу.")
            elif result is False:
                print("\033[31m⚠️ Эта книга уже выдана!")
            else:
                print("\033[31m Книга не найдена.")

        elif choice == "4":
            title = input("Введите название книги для возврата: ")
            result = library.return_book(title)
            if result is True:
                print("\033[32m Книга успешно возвращена.")
            elif result is False:
                print("\033[31m⚠️ Эта книга не числилась выданной.")
            else:
                print("\033[31m Книга не найдена.")

        elif choice == "5":
            print("\033[32mДо свидания!")
            break
        else:
            print("\033[31m Неверный выбор, введите число от 1 до 5.")

if __name__ == "__main__":
    main()