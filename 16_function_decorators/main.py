def log_function_call(func):
  def call():
    print("before function execution")
    func()
    print("After function execution")
  return call

@log_function_call
def say_hello():
  print("Function is being called")

say_hello()