class Count:
  def __init__(self, start):
    self.start = start
  
  def __iter__(self):
    return self
  
  def __next__(self):

    if self.start >= 0:
      num = self.start
      self.start -= 1
      return num 
    else:
      raise StopIteration

countdown = Count(10)

for counter in countdown:
  print(counter)