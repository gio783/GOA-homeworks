students = {
    "ანა": 8,
    "გიორგი": 9,
    "ნიკა": 10,
    "მარიამი": 9.5
}

best_student = max(students, key=students.get)
print(f"საუკეთესო ქულა აქვს {best_student}-ს → {students[best_student]}")

products = {
    "პური": 2.5,
    "რძე": 3.2,
    "კვერცხი": 5.0,
    "ყავა": 12.0
}

total = sum(products.values())
print(f"ჯამური ფასი: {total} ლარი")


books = {
    "ომი და მშვიდობა": "ლევ ტოლსტოი",
    "დონ კიხოტი": "მიგელ დე სერვანტესი",
    "პატარა პრინცი": "ანტუან დე სენტ-ეგზიუპერი"
}

search_title = "პატარა პრინცი"
if search_title in books:
    print(f"წიგნი '{search_title}' ეკუთვნის ავტორს: {books[search_title]}")
else:
    print("ასეთი წიგნი არ მოიძებნა.")



words = input("შეიყვანე სიტყვები (გამოყავი space-ით): ").split()
unique_words = set(words)
print("უნიკალური სიტყვები:", unique_words)


numbers = set(range(1, 11))
even_numbers = {x for x in numbers if x % 2 == 0}
even_list = list(even_numbers)
print("ლუწი რიცხვები ლისტში:", even_list)


ids = [101, 102, 103, 104, 101, 105]
unique_ids = set(ids)

if len(unique_ids) < len(ids):
    print("არის განმეორებული ID")
else:
    print("ყველა ID უნიკალურია") 