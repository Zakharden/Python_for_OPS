class Human():
    company = "Sber"

    def __init__(self, name: str, surname: str, age: int, prof: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.prof = prof

    def name(self):
        return self.name

    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) <= 0:
            raise ValueError("Что-то не то 🙃")


Zakhar = Human('Zakhar', 'Dvurechensky', 20, 'DevOps')
print(Zakhar.name())
Zakhar.set_name("Maria")
print(Zakhar.name())
Zakhar.set_name(123)





