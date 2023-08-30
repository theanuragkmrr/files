class library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def dispplayAvailBooks(self):
        print("Books Available in Library are: ")
        for book in self.books:
            print(book)
    def borrowBooks(self,bookName):
        if bookName in self.books:
            print(f"you borrow {bookName}")
            self.books.remove(bookName)
            return True
        else:
            print('Book is not availble in self')
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print(f"you have succesfully returned then book {bookName}")


class student:
    def reqestBook(self):
        self.book=input("Enter the book you want to Reqest: ")
        return self.book
    def returnBook(self):
        self.book=input("Enter the book you want to Return: ")
        return self.book

if __name__== "__main__":
    centralLibrary=library(["Hindi","English","Python","c","c++"])
    # centralLibrary.dispplayAvailBooks()
    while(True):
        print("""
        ====Welcome to Library===
        1.ENter 1 for list books.
        2.Reqest 2 to a book.
        3.Return 3 to book.
        4.Enter 4  for Exit
        """)
        a=int(input("Enter your choice: "))
        if a==1:
            centralLibrary.dispplayAvailBooks()
        elif a==2:
            centralLibrary.borrowBooks(student.reqestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        else:
            print("thanks for using central library")
            exit()