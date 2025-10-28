class User:
    def __init__(self, first_name, last_name, age, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.email = email

    def describe_user(self):
        print(f"\n\nUser Information:\n")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"\nHello, {self.first_name}! Welcome to the system.")



user1 = User("Tamar", "Kiria", 45, "Georgia", "tkiria@gmail.com")
user2 = User("Bob", "Brown", 32, "United States", "bob_brown@yahoo.com")
user3 = User("Elen", "Legran", 28, "France", "elen.l@hotmail.com")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
