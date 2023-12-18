def print_numbers():
    f = open("numbers.txt", "r")
    for i in (f.read()).split(","):
        print(i)
    f.close()

if __name__ == '__main__':
    print_numbers()