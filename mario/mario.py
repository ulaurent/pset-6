#define a function to be executed
def main ():
    height = -1;
    
    while height < 0  or height > 23:
        height = input("What is the Height? ")
        #print "Your height is: ", height
        type(height)
    
    for i in range (height):
        spaces = height -1
        for spaces in range (i):
           print (" ")
           spaces -= 1
    #}
    # //constructed for loop to generate the amount of x's needed per line;
    #// blocks starts at zero and increases as long as its less than or equal to i
        for blocks in range (i):
          print ("x")
   # }
#// new line command to begin new line before the first forloop adds ++1 to i
    #print ("\n");
#}
    
main()
    
    