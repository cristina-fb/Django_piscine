import sys

def get_cap_city(states, capital_cities, arg):
    if capital_cities.get(states.get(arg)) != None:
        print(capital_cities.get(states.get(arg)))
    else:
        print("Unknown state")

if __name__ == '__main__':

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    if len(sys.argv) == 2:
        get_cap_city(states, capital_cities, sys.argv[1])