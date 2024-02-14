# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# cities_visited = {}

# for country in travel_log:
#     cities_visited[country] = {
#         "Cities Visited": travel_log[country],
#         "Total Visits": len(travel_log[country])
        
#     }

# print(cities_visited)

# travel_log = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#     },
#     {
#     "country":"Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#     }
# ]

############################################################################################


# country = "Brazil" # Add country name
# visits = 2 # Number of visits
# list_of_cities = ["Sao Paulo", "Rio de Janeiro"] # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# # Do NOT change the code above 👆

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 

# def add_new_country(co, vi, li):
#     travel_log.append({
#         "country":co,
#         "visits":vi,
#         "cities":li
#         })


# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#############################################################################

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }

# print(order["main"][2])  # ['Steak']
# print(order["main"][2][0])  #Steak

#####################################################################

import os

# define our clear function
def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # Mac or Linux (aka posix)
    else:
        _ = os.system('clear')

def blind_auction():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

print("Welcome to the secret auction program\n")

bidders = {}

while True:
    blind_auction()
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    clear()
    if other_bidders != "yes":
        break

winner_name = max(bidders, key=bidders.get)
winning_bid = bidders[winner_name]

print(f"The winner is {winner_name} with a bid of ${winning_bid}.")
