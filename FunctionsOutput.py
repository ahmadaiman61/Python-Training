# def format_name(f_name,l_name):
#     if f_name== "" and l_name == "":
#         return "You didnt enter a valid input"
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     return f"{format_f_name} {format_l_name}"  ##return = end of the function, exit now

# print(format_name(input("What is your first name: "),input("What is your last name: ")))

#######################################################################################################

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return "Leap year"
#             else:
#                 return "Not leap year"
#         else:
#             return "Leap year"
#     else:
#         return "Not leap year"
  
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     month_days_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return_fx = is_leap(year)
#     month_calc = month - 1
#     if return_fx == "Leap year":
#         days = month_days_leap[month_calc]
#         return days
#     else:
#         days = month_days_normal[month_calc]
#         return days

# #🚨 Do NOT change any of the code below 
# year = int(input("Please enter the year: ")) # Enter a year
# month = int(input("Please enter the month: ")) # Enter a month
# days = days_in_month(year, month)
# print(days)

#################################################################################


import os
def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')

def selected_operator(operator_string,first_number, next_number):
    import operator

    operator_mapping = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow
    }

    selected_operator = operator_mapping.get(operator_string)
    return selected_operator(first_number, next_number)

def calculator(first_number, next_number):
    print('\n'.join(list_operator))
    operator_string = input("Pick an operation: ")
    result = selected_operator(operator_string,first_number, next_number)
    print(f"{first_number} {operator_string} {next_number} = {result}")
    return result
    

fn = int(input("What's the first number?: "))
nn = int(input("What's the next number?: "))
list_operator = ["+", "-", "*", "/"]

while True:
    results = calculator(fn, nn)
    cont_q = input(f"Type 'y' to continue calculating with {results}, or type 'n' to start a new calculation:  ").lower()
    if cont_q == "y":
        aa = int(input("What's the next number?: "))
        fn = results  # Update fn with the result
        nn = aa  # Update nn with the new number
    elif cont_q == "n":
        clear()
        fn = int(input("What's the first number?: "))
        nn = int(input("What's the next number?: "))





