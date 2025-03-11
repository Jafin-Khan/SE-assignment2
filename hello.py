name = ""
while not name.strip():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Please try again.")
print(f"Hello, {name}!")

