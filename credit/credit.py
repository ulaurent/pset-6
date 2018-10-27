import cs50

constant = 10
checkSum = 0

while True:
    cardNumber = input("Enter your card number: ")
    if len(cardNumber) == 15 or len(cardNumber) == 13 or len(cardNumber) ==16:
        break

print(len(cardNumber))

#Every other digit starting at second digit from the end
while constant <= (int)(cardNumber):
    lastDigit = (((int)(cardNumber)/constant)%(10))*2
    if lastDigit >= 10:
        checkSum += (lastDigit % 10)
        checkSum += ((lastDigit/10)%10)
    else:
        checkSum += lastDigit

    constant *= 100

constant = 1

#Every other digit starting at last digit from the end
while(constant <= (int)(cardNumber)):
    lastDigit2 = ((int)(cardNumber) / constant) % 10
    checkSum += lastDigit2

    constant *= 100

# Check if valid card Number
print(checkSum)
sumLastDigit = (checkSum % 10)
print(sumLastDigit)

if sumLastDigit == 0:
    print("Card Accepted")
elif sumLastDigit > 0:
    print("Card Denied")

if sumLastDigit == 0:

    if cardNumber > 1000000000000 and cardNumber < 10000000000000:
        print("VISA");

    elif cardNumber > 100000000000000 and cardNumber < 1000000000000000:
        print("AMEX");

    elif cardNumber > 1000000000000000 and cardNumber < 10000000000000000:
        type = ((cardNumber/1000000000000000)%10)
        if type == 5:
            print("MASTERCARD")
        elif type == 4:
            print("VISA");

