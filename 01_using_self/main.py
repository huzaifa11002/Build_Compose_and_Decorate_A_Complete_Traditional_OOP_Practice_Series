class Student():
  def __init__(self,name:str,marks:float):
    self.name = name
    self.marks = marks
  
  def display(self):
    print(f"Student Name: {self.name}")
    print(f"Marks: {self.marks}")

student1 = Student("Huzaifa", 53.45)
student1.display()