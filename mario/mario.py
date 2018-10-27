from cs50 import get_int

#define a function to be executed
def main ():
    while True:
        height = get_int("Height? ")
        if height > 0:
            break

    for i in range (height-1,-1,-1):
        for j in range (i):
            print (" ", end="")
        for k in range((height-i)*2+2):
            if k == (height-i) or k == (height-i)+1:
                print(" ", end="")
            else:
                print("#", end="")

        print(" ")


if __name__=="__main__":
    main()


