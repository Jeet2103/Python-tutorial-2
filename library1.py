class Library:
    num_books = 0
    num_users = 0
    total_price = 0

    def __init__(self, book_name, book_price, user_name):
        self.book_name = book_name
        self.book_price = book_price
        self.user_name = user_name

        if book_name:
            Library.num_books += 1
            Library.total_price += book_price

        if user_name:
            Library.num_users += 1

    def display_book_details(self):
        if self.book_name:
            print(self.book_name)
            print(self.book_price)

    def display_user_details(self):
        if self.user_name:
            print(self.user_name)


while True:

    option = input("Enter 'u' for new user or 'b' for new book: ")

    if option == 'b':
        book_name = input("Enter the book name: ")
        book_price = float(input("Enter the price of the book: "))
        book = Library(book_name, book_price, None)
        book.display_book_details()

    elif option == 'u':
        user_name = input("Enter the user name: ")
        user = Library(None, 0, user_name)
        user.display_user_details()

    choice = input("Want to continue? 1/0: ")
    if choice == '0':
        break


print("\nTotal number of users in the library:", Library.num_users)
print("Total number of books in the library:", Library.num_books)
print("Total price of books in the library:", Library.total_price)