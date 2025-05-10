class Multiplier:
  def __init__(self, factor:int):
    self.factor = factor

  def __call__(self, value:int):
    return value * self.factor

a = Multiplier(30)
print(callable(a)) # print True

print(a(2)) # print 60