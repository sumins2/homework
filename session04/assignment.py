
# 과제 1. 별찍기 (4월 20일까지)
# - 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
# **********
# *********
# ********
# *******
# *****
# ****
# ***
# **
# *

i=10
while i > 0:
    
    i= i-1
    if i == 6:
        continue
 

    print('*'*i)
        


# 과제 2. 구구단 (4월 20일까지)
# - 구구단 2단을 출력해보세요!
i = 1
while i < 10 :
    print('2 x',i, '=', 2*i)
    i = i+1
    
# 과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)
n = 1
sum = 0
while n < 1001:
    n +=1
    if n%3 ==0:
        sum += n
print(sum)

# 과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum = 0
for i in mutsa_scores:
    sum = sum + i
average = sum / len(mutsa_scores)
print("평균=", average)
    
# 과제 5. input.py 문제 2개 풀기 (4월 20일까지)

# 과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
# - 이미지 자율
# - 까먹기전에 해주세요~

