class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Марка автомобиля: {self.brand}, модель: {self.model}, год выпуска: {self.year}")
moskvich = Car("Москвич", "Москвич 3", "2022")
moskvich.info()