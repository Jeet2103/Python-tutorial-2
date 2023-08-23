class Library:
    num_books = 0
    num_users = 0
    total_price = 0

    def __init__(self, book_name=None, book_price=0, user_name=None):
        self.book_name = book_name
        self.book_price = book_price
        self.user_name = user_name
    
    def display_book_details(self):
        if self.book_name:
            print(f"Book Name: {self.book_name}\nBook Price: {self.book_price}")
        else:
            print("No book details available.")

    def display_user_details(self):
        if self.user_name:
            print(f"User Name: {self.user_name}")
        else:
            print("No user details available.")

    def input(self):
        while True:

            option = input("Enter 'u' for new user or 'b' for new book: ")

            if option == 'b':
                self.book_name = input("Enter the book name: ")
                self.book_price = float(input("Enter the price of the book: "))
                self.display_book_details()
                Library.num_books += 1
                Library.total_price += self.book_price

            elif option == 'u':
                self.user_name = input("Enter the user name: ")
                self.display_user_details()
                Library.num_users += 1
                

            choice = input("Want to continue? 1/0: ")
            if choice == '0':
                break

# Taking input and initializing instances from user input
books = Library()
books.input()


# Displaying total numbers of users, total numbers of books, and total price of books
print("\nTotal Number of Users:", Library.num_users)
print("Total Number of Books:", Library.num_books)
print("Total Price of Books:", Library.total_price)
