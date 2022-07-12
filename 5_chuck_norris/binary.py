# # 10진수를 2진수로 변환하여 반환하는 함수
# def to_binary(decimal):
#     binary = ""  # 2진수 문자열을 담을 자료형 준비

#     # 2로 나눠가면서 나머지를 더하기때문에 남은 숫자가 0이 될때까지 반복
#     while decimal >0 :
#         remainder=decimal%2 # 2로 나눈 나머지
#         binary+=str(remainder) # 숫자를 문자로 변환해서 병합한다
#         decimal=decimal//2 # decimal이 0이 될때까지 계속 2로 나눈다
#     return binary[::-1]

# print(to_binary(67))

codes = "1000011" # 대문자 C의 2진수 표현
previous_bit = ""

for bit in codes:
    if bit != previous_bit:
        print("다름")
    else:
        print("같음")

    previous_bit = bit # 반복문의 끝에서 현재 비트를 이전비트에 대입해야 한다