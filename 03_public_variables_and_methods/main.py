class Car():
  def __init__(self):
    self.brand = "Toyota"

  def start(self):
    print("Engine Start")

car1 = Car()
print(car1.brand)
car1.start()