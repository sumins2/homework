#실습 2번
def gugudan_odd():
    i = 1
    while i <10:
        for j in range(1, 10):
            print("%d*%d" % (i,j))
        i += 2

def gugudan_even():
    i = 2
    while i <10:
        for j in range(1, 10):
            print("%d*%d" % (i,j))
        i += 2

def gugudan_odd_or_even(num):
    if(num % 2 == 0):
        gugudan_even()
    else:
        gugudan_odd()

gugudan_odd_or_even(3)
print(gugudan_odd_or_even)

# 실습 3번
def gugudan_input(num):
    i= 1
    while i <= num:
        for j in range(1,10):
            print("%d*%d" % (i, j))
        i+=1

gugudan_input(5)
print(gugudan_input)

