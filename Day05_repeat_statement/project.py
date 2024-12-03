# random 모듈에서 사용할만한 친구들 가져오기
from random import shuffle, choice

# 문자, 숫자, 기호 리스트 정성
# chr를 사용하여 ASCII로 접근할 수 있으나 아직 배우지 않은 내용이기에 일단 작성
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 사용자 입력 받기
print("Welcome to the PyPassword Generator!")
total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

# 유효성 검증
if total_letters < total_symbols + total_numbers:
    print("Error: The number of letters must be greater than or equal to the total number of symbols and numbers.")
else:
    # 비밀번호 생성
    password_list = []

    # 문자 추가
    for _ in range(total_letters - total_symbols - total_numbers):
        password_list.append(choice(letters))
    
    # 숫자 추가
    for _ in range(total_numbers):
        password_list.append(choice(numbers))
    
    # 기호 추가
    for _ in range(total_symbols):
        password_list.append(choice(symbols))
    
    # 비밀번호 리스트 출력
    print(password_list)

    # 비밀번호 섞기
    shuffle(password_list)

    # 섞은 비밀번호 출력
    print(password_list)

    # 리스트를 문자열로 변환
    # 반복문을 돌며 password 생성
    password = ""
    for char in password_list:
        password = password + char
    
    # 아래와 같이 join을 이용할 수도 있으나 배우지 않아 패스
    # password = ''.join(password_list)
    print(f"Your generated password is: {password}")
