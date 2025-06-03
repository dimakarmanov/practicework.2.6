class Nikola:
    __slots__ = ['name', 'age']
    def __init__(self, name, age, surname):
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай."
        self.age = age
        self.surname = surname

nikola = Nikola("Николай", 18, "Алексеевич")
ivan = Nikola("Иван", 17, "Андреевич")
print(nikola.name)
print(ivan.name)
print(nikola.surname)