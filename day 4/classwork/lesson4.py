num1=5
num2=8

result=num1+num2
 
print(result)
 
class Debater:
    def __init__(self, name, side):
        self.name, self.side, self.args = name, side, []  # ვინ არის დებატანტი და მისი მხარე
    
    def add(self, arg):
        self.args.append(arg)  # ამატებს არგუმენტს
    
    def show(self):
        print(f"{self.name} ({self.side}):", *self.args, sep="\n- ")  # აჩვენებს არგუმენტებს

# დებატანტები და არგუმენტები
d1, d2 = Debater("გიორგი", "მხარდამჭერი"), Debater("ნიკა", "მოწინააღმდეგე")
(d1, d2), ("ტექნოლოგია აუმჯობესებს განათლებას.", "ინოვაციები ამარტივებს ცხოვრებას."), ("ტექნოლოგია ზრდის მარტოობას.", "სმარტფონები ამცირებენ კონცენტრაციას.")

# შედეგი
d1.show(), d2.show()


num1=6
num2=40

result=num1+num2

print(result)

num=15
num=10

print(num)
 