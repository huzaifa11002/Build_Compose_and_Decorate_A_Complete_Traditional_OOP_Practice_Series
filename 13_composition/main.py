class Engine():

  def engine_status(self):
    print("Start Engine...")

class Car():
  def __init__(self):
    self.engine = Engine()

  def start(self):
    self.engine.engine_status()
    print("Car is running 🚙")

car1 = Car()
car1.start()