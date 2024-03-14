# def greet():
#     print("1")
#     print("2")
#     print("3")

# greet()

# def greet_with_name(name):
#     print(f"Number is {name}")
#     print(f"Age is {name}")
#     print(f"Calorie is {name}")
#     print(type(name))

# greet_with_name(25)

# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Aiman","Kemaman")

# def greet_with(a=1,b=2,c=3):
#     print(a)
#     print(b)
#     print(c)


# def prime_checker(number):
#   prime_number = False
#   counter_primenumber = 0
#   for check in range(1,100):
#     if number % check == 0:
#       counter_primenumber += 1
#   if counter_primenumber <= 2:
#     print("It's a prime number.")
#   else:
#     print("It's not a prime number.")

# n = int(input())
# prime_checker(number=n)

def caesar(text,shift,ops):
    
    result = []
    listed = list(text)
    count = len(listed) ### len show real number count 1-...
    for position in range(count):   ### The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
        shifted = (op_func(alphabet.index(listed[position]),shift)) % 26  ##use the modulo operator % to wrap around the index if it exceeds 25.
        result += alphabet[shifted]
    new_string = "".join(result)
    print(f"The {direction}d text is {new_string}")

decision = True
while decision == True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    import operator

    ops = {
        "+" : operator.add,
        "-" : operator.sub
    }

    if direction == 'encode':
        op_char = "+"
    else:
        op_char = "-"

    op_func = ops[op_char]

    caesar(text,shift,ops)

    decision = input(f"Do you want to restart the program?\n").lower()
    if decision == "yes":
        decision = True
    else:
        decision = False