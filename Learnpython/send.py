class lib:
    def __init__(self,list,name):
        self.BookList=list
        self.name=name
        self.lendDict={}
    def displaybooks(self):
        print(f"Welcome to my Liberary books are availble are :,{self.name}")
        for book in self.BookList:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Boook loist updated")
        else:
            print(f"book is alredy taken by: {self.lendDict[book]}")
    def addBook(self,book):
        pass
    def returnBook(self,book):
        pass