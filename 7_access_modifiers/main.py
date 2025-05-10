class Empolyee():

  def __init__(self):
    self.name = "Huzaifa"; # public variable
    self._salary = 10000   # protected variable using one underscore (_) in starting
    self.__ssn = 304210    # private variable using two underscore (__) in starting

empolyee1 = Empolyee()
print(empolyee1.name)  
print(empolyee1._salary) 
print(empolyee1.__ssn)