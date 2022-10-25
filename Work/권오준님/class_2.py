class Students:
    def __init__(self, name,kor, math, eng, sci):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci

    def sum(self):
        return self.kor + self.math + self.eng+ self.sci

    def average(self):
        return self.sum()/4

    def test_result(self):
        # return f"{self.name}\t{self.kor}\t{self.math}\t{self.eng}
        # \t{self.sci}\t{self.sum}\t{self.average()}"

        # average()가  <bound method Students.sum of <__main__.Students object at 0x0000024CFC8384C8>>
        # 라고 뜸
        
        return f"{self.name}\t{self.kor}\t{self.math}\t{self.eng}\t{self.sci}\t{self.sum()}\t{self.average()}"

students = [
    Students("카리나",84,86,75,99),
    Students("우기  ",90,56,85,88),
    Students("미연  ",91,92,76,77),
    Students("장원영",95,97,80,89),
    Students("신세경",96,93,99,83),
    Students("사나  ",70,89,95,95)
]

print("="*70)
print("이름\t국어\t수학\t영어\t과학\t총점\t평균\n")
for i in students:
    print(i.test_result())
print("="*70)