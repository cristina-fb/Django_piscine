import sys

def get_state(states, capital_cities, arg):
    for key, value in states.items():
        if arg == value:
            return key

def print_country_cities(states, capital_cities, arg):
    print_var = None
    for i in arg.split(","):
        i = i.strip()
        if len(i) == 0:
            continue
        for key, value in states.items():
            if key.lower() == i.lower():
                print_var = capital_cities[value] + " is the capital of " + key
                break
        if (print_var == None):
            for key, value in capital_cities.items():
                if value.lower() == i.lower():
                    print_var = value + " is the capital of " + get_state(states, capital_cities, key)
                    break
            if (print_var == None):
                print_var = i + " is neither a capital city nor a state"
        print(print_var)
        print_var = None

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
        print_country_cities(states, capital_cities, sys.argv[1])