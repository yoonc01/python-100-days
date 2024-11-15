bill = float(input("What was the total bill? $"))
percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
cnt = int(input("How many people to split the bill? "))

tip = round((bill * (100 + percent) / 100) / cnt, 2)
print(f"Each person should pay: ${tip}")