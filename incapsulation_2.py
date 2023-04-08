class Human():
    company = "Sber"

    def __init__(self, name: str, surname: str, age: int, prof: str):
        self.__name = name
        self.surname = surname
        self.age = age
        self.prof = prof

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) <= 0:
            raise ValueError("Что-то не то 🙃")
        self.__name = new_name


Zakhar = Human('Zakhar', 'Dvurechensky', 20, 'DevOps')
print(Zakhar.name)
Zakhar.name = "Ivan"
print(Zakhar.name)