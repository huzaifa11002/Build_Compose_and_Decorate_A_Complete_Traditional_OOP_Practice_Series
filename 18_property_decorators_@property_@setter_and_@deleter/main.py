class Product:

  def __init__(self, price:int):
    self._price = price

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, new_price):
    self._price = new_price
    return self._price

  @price.deleter
  def price(self):
    del self._price
    print("Product price deleted...")

product1 = Product(3000)
print(product1.price)
product1.price = 2300
print(product1.price)
del product1.price