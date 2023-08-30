# imp=int(input("Enter number of Items to insert"))
# ls=[]
# for i in range(imp):
#     a=input(f"no. inserted {i+1}")
#     ls.append(a)
# print("Enter the comprehension to be converted")
# print("1.list\n2.Dictionary\n3.set")
# c=int(input("Enter your choice"))
# if c==1:
#     print(ls)
# elif c==2:
#     dict={i: j for i,j in enumerate(ls)}
#     print(dict)
# elif c==3:
#     set={i for i in ls}
#     print(set)
# else:
#     print("Invalid choice, Try agein !!!")




# n=int(input("enter a number to print its table"))
# table=[n*i for i in range(1,11)]
# print(table)
# n=int(input("Enter number"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1
#
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print(
                "Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while (True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else: