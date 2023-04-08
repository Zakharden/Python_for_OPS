from incapsulation_2 import Human


class Humannode(Human):
    qtty_legs = 4

    def about_mybusiness(self, qtty_years):
        print(f'Пишу на Pythobnn уже {qtty_years} лет')


Zakharchik = Humannode("Zakharchik", "Dvurechernsky", 12, "DevOPsik")
print(Zakharchik.name)

Zakharchik.about_mybusiness(17)
