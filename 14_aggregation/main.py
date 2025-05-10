class Department():

  def __init__(self, name, empolyees):
    self.name = name
    self.employees = empolyees

  def office_time(self):
    print("office is starting...")

    for empolyee in self.employees:
      empolyee.work()

class Employeee():

  def __init__(self, name):
    self.name = name

  def work(self):
    print(f"{self.name} is now working")


empolyee1 = Employeee("Huzaifa")
empolyee2 = Employeee("Zara")

depart = Department("ABC Department", [empolyee1, empolyee2])

depart.office_time()