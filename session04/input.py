# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')
phone_num = input("전화번호를 입력하세요 :")
phone_num = phone_num.replace('-','').replace('.','').replace(',','').replace(' ','')
print(phone_num)

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')

name = input("영어 이름을 입력하세요 :")
split_name = name.title().split( )
first_name = split_name[0]
last_name = split_name[1]
print('first name :',first_name,'last name :', last_name)