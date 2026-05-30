def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Vraj"))
print(greet("Vraj", "Good morning"))
print(greet("Vraj", "Namaste"))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))


def total(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(type(numbers))
    return sum


print(total(1, 2))
print(total(1, 2, 3, 4, 5))
print(total(10, 20, 30, 40, 50, 60))


def print_info(**details):
    print(type(details))
    for key, value in details.items():
        print(f"{key}:{value}")


print_info(name="Vraj", city="Vadodara", role="developer")

x = "global"


def show_scope():
    # x = "local"

    # Since there is no local scope of x in the function python finds if there are any in the global level which is there
    print(f"Inside function: {x}")


# This show the local scope of x thats why it prints "local"
show_scope()

# This show the global scope of x thats why it prints "Global"
print(f"Outside function: {x}")
