#define a function to be executed
def main ():
    height = -1;
    
    while height < 0  or height > 23:
        height = input("What is the Height? ")
        #print "Your height is: ", height
        #type(height)
    
for i in range(height-1, -1, -1):
        for j in range(i):
            print(" ", end= "")
        for k in range((height-i)*2+2):
            if k == (height-i) or k == (height-i)+1:
                print(" ", end="")
            else:
                print("#", end="")

        print("")

if __name__=="__main__":
    main()

    
    