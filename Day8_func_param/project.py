#def encrypt(original_text, shift_amount):
#    encrypted_text = ""
#    #사실 map을 쓰는 것이 더 효율적으로 보임
#    for letter in original_text:
#        new_idx = (alphabet.index(letter) + shift_amount) % 26
#        encrypted_text = encrypted_text + alphabet[new_idx]
#    print(f"Here is the encoded result: {encrypted_text}")
#
#def decrypt(original_text, shift_amount):
#    decrypt_text = ""
#    for letter in original_text:
#        new_idx = (alphabet.index(letter) - shift_amount) % 26
#        decrypt_text = decrypt_text + alphabet[new_idx]
#    print(f"Here is the decoded result: {decrypt_text}")

# 위의 함수는 너무 겹치는 것이 많아 하나로 합치고 매개변수를 하나 더 선언하여 encrypt인지 decrypt인지 구분하게 할 수 있음
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        if letter not in alphabet:
            output_text = output_text + letter
        else:
            new_idx = (alphabet.index(letter) + shift_amount) % 26
            output_text = output_text + alphabet[new_idx]
    # encode_or_decode에는 encode, decode 문자열을 받는다.
    # 그래서 encoded, decoded를 아래와 같이 {encode_or_decode}d 로 작성할 수 있음
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# alphabet을 다 치는 것보다는 import string을 이용하여 alphabet = string.ascii_lowercase를 받아도 됨 다만 자료형이 달라짐
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while (True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: " ).lower()
    # direction 값이 잘못 들어오면 오류 출력 및 다시 입력 유도
    while(direction != "encode" and direction != "decode"):
        print("Wrong Input. Type 'encode' or 'decode'")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: " ).lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(text, shift, direction)
    do_process = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # direction과 같이 값이 잘못 들어오면 오류 출력 및 다시 입력 유도
    while (do_process != "yes" and do_process != "no"):
        print("Wrong Input. Type 'yes' or 'no'")
        do_process = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if do_process == "no":
        print("GoodBye!")
        break

# 위의 유효 입력 체크하는 것도 방식이 유사하므로 하나의 함수를 작성해도 좋을 거 같음

