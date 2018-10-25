from cs50 import get_int

def main():
    x = get_int("What is your first number: ")
    y = get_int("What is your second number: ")

    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} and {y} are equal")

if __name__ == "__main__":
    main()
