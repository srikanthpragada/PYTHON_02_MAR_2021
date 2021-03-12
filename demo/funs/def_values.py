def greet(name = "Guest", message='Hello'):
    print(f"{message}, {name}")


greet("Tom", "Hi")
greet("Bill")
greet()
greet(message = "Hi")
