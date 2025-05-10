class Dog():

  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"Dog name: {self.name}")
    print(f"Dog Breed: {self.breed}")

dog = Dog("Feezu", "German Shepherd")
dog.bark()