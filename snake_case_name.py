name = (input("Enter your full name in incorrect casings please: "))
snake = (name.lower().replace(" ", "_"))#replace spaces with _

print(snake)