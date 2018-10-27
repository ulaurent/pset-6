from cs50 import get_float

count = 0

while True:
    change = get_float("How much change is owed: ")*100
    if change > 0:
        break

while change > 0:
    if change >= 25:
        count += 1
        change -= 25
    elif change >= 10:
        count += 1
        change -= 10
    elif change >= 5:
        count += 1
        change -= 5
    elif change >= 1:
        count += 1
        change -= 1

print(f"The total number of coins is {count}")


