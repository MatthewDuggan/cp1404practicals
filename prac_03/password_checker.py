MIN_LENGTH = 10


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input("input your password: ")
    while len(password) < MIN_LENGTH:
        print("The password does not reach the required length")
        password = input("input your password: ")
    return password


def print_asterisks(password):
    for _ in password:
        print("*", end="")


main()
