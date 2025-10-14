class library:
    def __init__(self,books,title):
        self.books=books
        self.title=title

    def showbooks(self):
        print(f"{self.title} {self.books}is in library")

class student(library):
   # def __init__(self,name,age,books,title):
        self.name=name
        self.age=age
        #library.__init__(self,books,title)

    def showbooks(self):
        print(f"{self.name} {self.age} is student is having {self.title} book")

lib=library(100,"python")
lib.showbooks()
lib1=library(200,"java")
lib1.showbooks()
stu=student("ajay",23,300,"c++")
stu.showbooks()