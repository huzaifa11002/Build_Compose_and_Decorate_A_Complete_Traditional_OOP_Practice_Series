class Bank():
  bank_name = "Upwork"

  @classmethod
  def change_bank_name(cls,name):
    cls.bank_name = name

# Instance
acc1 = Bank()
acc2 = Bank()
acc3 = Bank()

# Print Bank Name
print("Before Changing Bank Name:\n")
print(acc1.bank_name)
print(acc2.bank_name)
print(acc3.bank_name)

# Change Bank Name
Bank.change_bank_name("Fiverr")

# Change Bank Name same object
print("\nAfter Changing Bank Name:\n")
print(acc1.bank_name)
print(acc2.bank_name)
print(acc3.bank_name)