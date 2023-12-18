import sys

def get_state(states, capital_cities, arg):
    for key, value in capital_cities.items():
        if arg == value:
            for key1, value1 in states.items():
                if key == value1:
                    print(key1)
                    return
    print("Unknown capital city")

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
        get_state(states, capital_cities, sys.argv[1])