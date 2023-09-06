class library:
    def __init__(self):
        self.book_list=[]
        self.number_books=0
    def add_books(self,books):
        self.book_list.append(books)
        self.number_books= len(self.book_list)
    def info(self):
       print(f"Number of Books :- {self.number_books}")
       for i in self.book_list:
           print(i)

a=library()
a.add_books("'Harry Porter'")
a.add_books("'To Kill a Moking bird'")
a.add_books("'Byomkesh'")
a.info()
