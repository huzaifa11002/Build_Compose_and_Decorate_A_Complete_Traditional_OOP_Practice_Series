class InvalidAgeError(Exception):
  pass

def checkAge(age):
  if age < 18:
    raise InvalidAgeError("You should must be equal and greater than 18.")

try:
  user_age = int(input("Enter your age: "))
  checkAge(user_age)
  print("You are Eligible")
except Exception as e:
  print(e)
  
