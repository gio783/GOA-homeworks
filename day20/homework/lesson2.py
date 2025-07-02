animals = ["Dog", "Cat", "Elephant", "Fox", "Bear", "wolf", "Lion"]

for animal in animals:
    if len(animal) < 5 and animal.istitle():
        print(animal[:3])  
    else:
        print(f"{animal} - ეს სიტყვა გრძელია")
