import os

print("Welcome to the secret auction program")
data = {}
while(True):
    name = input("What is your name: ")
    bid = int(input("What's your bid?: $"))
    while(bid < 0):
        print("bid should be more than or equal to 0")
        bid = int(input("What's your bid?: $"))
    data[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while(should_continue != "yes" and should_continue != "no"):
        print("Wrong input. Type 'yes' or 'no'")
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        break
    os.system("cls" if os.name == "nt" else "clear")



max_bid = 0
winner = ""

for name in data:
    # 가격이 같은 경우는 먼저 등록한 사람이 입찰자
    # 3.7 이상에서는 dict은 입력 순서를 유지
    if data[name] > max_bid:
        max_bid = data[name]
        winner = name

print(f"The winner is {winner} with a bid of ${max_bid}.")

