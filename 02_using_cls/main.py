class Counter():
  count = 0
  def __init__(self):
    Counter.count += 1

  @classmethod
  def show_count(cls):
    print(f"Total Object count is : {cls.count}")


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()

Counter.show_count()