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


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.\


def encrypt(text,shift):
    
    result = []
    listed = list(text)
    count = len(listed) ### len show real number count 1-...
    for position in range(count):   ### The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
        shifted = (alphabet.index(listed[position]) + shift) % 26  ##use the modulo operator % to wrap around the index if it exceeds 25.
        result += alphabet[shifted]
    new_string = "".join(result)
    print(f"The encoded text is {new_string}")

encrypt(text,shift)





    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 