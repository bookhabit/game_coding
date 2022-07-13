# 10진수를 2진수로 변환하여 반환하는 함수
from email import message


def to_binary(decimal):
    binary = ""  # 2진수 문자열을 담을 자료형 준비

    # 2로 나눠가면서 나머지를 더하기때문에 남은 숫자가 0이 될때까지 반복
    while decimal >0 :
        remainder=decimal%2 # 2로 나눈 나머지
        binary+=str(remainder) # 숫자를 문자로 변환해서 병합한다
        decimal=decimal//2 # decimal이 0이 될때까지 계속 2로 나눈다

    # 2 진수 문자열의 길이가 6일 경우 0을 붙여준다
    if len(binary)==6 :
        binary += "0"
    return binary[::-1]
    
def chuck_norris_encoding(codes) :
    # codes = "1000011" # 대문자 C의 2진수 표현
    previous_bit = ""
    count = 0 # 연속된 값만큼 0을 추가해주기 위해 
    answer = ""

    for bit in codes:
        # 두 비트가 다르면서 count가 0 이상일 경우에만 처리
        if bit != previous_bit and count >0:
            # 1이면 0  , 0이면 00 
            if previous_bit == "1":
                answer += "0 "  # 0이나 00 뒤에 공백이 들어가야 하므로 공백문자도 함께 추가
            else:
                answer += "00 "

        # count개수만큼 0을 추가하고 공백도 추가  곱하기는 개수만큼 0을 추가해준다
        answer += "0" * count +" "
        # count 개수만큼 0을 추가하였으므로 이를 초기화
        count = 0

        count +=1 # 0과 1에 상관없이 비트의 개수는 매번 증가시킴
        previous_bit = bit # 반복문의 끝에서 현재 비트를 이전비트에 대입해야 한다

    if previous_bit == "1":
            answer += "0 "
    else:
            answer += "00 "

    answer += "0" * count
    print(answer)

# 문제풀이 
# 문자를 아스키 코드로 변환하기  ord함수

message = input()

binary_string = ""
for ch in message:
    binary_string += to_binary(ord(ch))

encoded_message = chuck_norris_encoding(binary_string)
print(encoded_message)