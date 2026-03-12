class LibraryBook:

    def __init__(self, name, price):
        self.book_name = name      # public variable
        self.__book_price = price  # private variable

    def set_price(self, price):
        self.__book_price = price

    def get_price(self):
        return self.__book_price


class DigitalBook(LibraryBook):

    def update_price(self, new_price):
        self.set_price(new_price)


book = DigitalBook("Python Programming", 500)

print("Book Name:", book.book_name)
print("Original Price:", book.get_price())

book.update_price(600)

print("Updated Price:", book.get_price())