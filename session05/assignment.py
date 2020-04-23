class Fourcal:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.add_num = 0
        self.sub_num = 0
        self.mul_num = 0
        self.div_num = 0
    
    def add(self, a, b):
        self.add_num += 1
        return a+b
    def sub(self, a, b):
        self.sub_num += 1
        return a-b
    def mul(self, a,b):
        self.mul_num += 1
        return a*b
    def div(self, a,b):
        self.div_num += 1
        if(b == 0):
            print('0으로 나눌 수 없습니다')
            return None
        return a/b      

    def Showcount(self):
        
        print("덧셈 :", self.add_num)
        print("뺄셈 :", self.sub_num)
        print("곱셈 :", self.mul_num)
        print("나눗셈 :", self.div_num)

    

calculator1 = Fourcal("박수민", 22, "korea uiversity")

calculator1.add(4,2)
calculator1.Showcount()
