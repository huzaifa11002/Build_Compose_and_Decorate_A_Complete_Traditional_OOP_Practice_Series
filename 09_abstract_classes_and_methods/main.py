from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):

  def __init__(self, width:int, height:int):
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height

rectangle = Rectangle(3,5)
print(f"Area of a Rectangle is : {rectangle.area()}")