def greet(name):
    message = "Hello, " + name + "!" # Deliberate typo: messsage
    print(message)

def add(a, b):
    return a + b

greet("Tester")
print(f"Sum: {add(5,3)}")
