class A:
  def show(self):
    print("A class method")

class B(A):
  def show(self):
    print("B class method")

class C(A):
  def show(self):
    print("C class method")

class D(C,B):
  pass

d = D()
d.show() # class B method running because MRO (D->B->C->A)