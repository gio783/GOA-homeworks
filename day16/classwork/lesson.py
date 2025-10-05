i = 1
while i <= 20:
    print(i)
    i += 1

original_pin = "1234"  
entered_pin = input("enter pin code: ")

while entered_pin != original_pin:
    print("incorect,try again.")
    entered_pin = input("enter pincode: ")

print("corect!")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

for i in range(1, 31):
    if i % 2 != 0:
        print(i)

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
