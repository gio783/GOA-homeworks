
word = input("შემოიტანეთ სიტყვა: ")

print(word.lower())      
print(word.upper())     
print(word.capitalize()) 


sentence1 = input("შემოიტანეთ პირველი წინადადება: ")
sentence2 = input("შემოიტანეთ მეორე წინადადება: ")
sentence3 = input("შემოიტანეთ მესამე წინადადება: ")

print(sentence1.lower())     
print(sentence2.upper())      
print(sentence3.capitalize()) 
my_name = "გიორგი"  
user_name = input("შენი სახელი: ")


if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")


sentence = "ეს არის წინადადება რომელიც უნდა გადავაქციოთ"  
print(sentence.capitalize())



"""
lower()  გარდაქმნის ყველა ასოს პატარა ასოდ.
მაგ: "HELLO".lower() ➡ "hello"

.upper() –გარდაქმნის ყველა ასოს დიდ ასოდ.
მაგ: "hello".upper() ➡ "HELLO"

.capitalize() მხოლოდ პირველი ასო დიდად, დანარჩენი პატარა.
მაგ: "heLLo".capitalize() ➡ "Hello"

.title() თითოეული სიტყვის პირველი ასო დიდია.
მაგ: "hello world".title() ➡ "Hello World"

.strip()  აშორებს ზედმეტ სივრცეებს (space) თავიდან და ბოლოში.
მაგ: "   hello   ".strip() ➡ "hello"

lstrip() აშორებს სივრცეებს მხოლოდ მარცხენა მხარეს.
მაგ: "   hello".lstrip() ➡ "hello"

rstrip()  აშორებს სივრცეებს მხოლოდ მარჯვენა მხარეს.
მაგ: "hello   ".rstrip() ➡ "hello"

replace(old, new)  ცვლის სტრინგში ერთ მნიშვნელობას მეორით.
მაგ: "I like dogs".replace("dogs", "cats") ➡ "I like cats"

split() ყოფს სტრინგს სიტყვებად და აბრუნებს სიას.
მაგ: "a,b,c".split(",") ➡ ['a', 'b', 'c']

join() –სიას აერთიანებს სტრინგში მითითებული გამყოფით.
მაგ: ",".join(['a', 'b', 'c']) ➡ "a,b,c"

find()  პოულობს სიმბოლოს ან სიტყვის ადგილს სტრინგში (პირველი შესატყვისი).
მაგ: "hello".find("e") ➡ 1

startswith(value) ამოწმებს იწყება თუ არა სტრინგი მოცემული სიტყვით.
მაგ: "hello".startswith("he") ➡ True

endswith(value)  ამოწმებს მთავრდება თუ არა სტრინგი მოცემული სიტყვით.
მაგ: "hello".endswith("lo") ➡ True
"""
