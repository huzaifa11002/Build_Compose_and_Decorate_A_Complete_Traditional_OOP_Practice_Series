class Book():
  totalbook= 0

  def __init__(self, name):
    self.name = name
    print(f"{self.name} is added successfully")
    Book.increment_book_count()
  
  @classmethod
  def increment_book_count(cls):
    cls.totalbook += 1
    print(f"Total books is: {cls.totalbook}")

book1 = Book("You and Me")
book2 = Book("Ashique")

Book.increment_book_count()