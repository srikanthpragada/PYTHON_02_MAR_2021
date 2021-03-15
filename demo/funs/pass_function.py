def process(name, func):
    func(name)


def wish(name):
    print("Hello,", name)


def greet(name, message = "Hi"):
    print(message, name)


process("Stephens", wish)
process("Stephens", greet)
