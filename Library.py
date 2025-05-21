class Library:
    
    
    def __init__(self):
        self.books=[]
        
    def book_entry(self):
     while True:
        name=input("Enter name of book (or press Enter to finish): ")
        if not name :
         break
        author= input("Enter name of  book author (or press Enter to finish): ")
        if not author :
         break
     
        book={"name": name , "author":author}
        self.books.append(book)

    
    def get_book_count(self):
       no_of_books = len(self.books)
       print(f"The library has {no_of_books}book/books")


l=Library()
l.book_entry()
l.get_book_count()

#Or 

# class Library2:
  
#  No_books=0
#  def __init__(self,name):
#    self.name= name
#    Library2.No_books +=1
#  def get_book_count(self):
#    print(f"The Library has {self.No_books} books")

# l1=Library2("Too good to be true")
# l1.get_book_count()
# l2=Library2("2 States")
# l2.get_book_count()

   
   

     