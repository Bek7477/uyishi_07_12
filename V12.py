class Mashina:
    def __init__(self, nomi, turi, ishlab_ch_yili, narxi = 4000) -> None:

        self.nomi = nomi
        self.turi = turi
        self.ishlab_ch_yili = ishlab_ch_yili
        self.narxi = narxi

    def malumot(self):
        return (f"Mashina nomi: {self.nomi}, Turi: {self.turi},"f"Narxi: $ {self.narxi}, Ishlab chiqarilgan yili: {self.ishlab_ch_yili}")

mashinalar = [
    Mashina("Chevrolet Spark", "Yengil", 2018, 8000),
    Mashina("Chevrolet Malibu", "Yengil", 2019, 15000),
    Mashina("Toyota Camry", "Yengil", 2017, 20000),
    Mashina("Ford F-150", "Yuk avtomabili", 2015, 30000),
    Mashina("BMW X5", "Yengil", 2020, 45000),
    Mashina("Hyundai Elantra", "Yengil", 2016, 13000),
    Mashina("Honda Civic", "Yengil", 2018),
    Mashina("Mercedes-Benz Actros", "Yuk avtomobili", 2019, 70000),
    Mashina("Nissan Navara", "Yuk avtomobili", 2017, 28000),
    Mashina("Tesla Model 3", "Yengil", 2020, 35000)
] 

saralash = sorted(mashinalar, key=lambda x: x.ishlab_ch_yili)
for mashina in saralash:
    print(mashina.malumot())
    