class Soda:
    def __init__(self, supplement = "Апельсин"):
        self.supplement = supplement

    def show_my_drink(self):
        if self.supplement:
            print(f"Газировка и {self.supplement}")
        else:
            print("Обычная газировка")

soda = Soda()
soda.show_my_drink()