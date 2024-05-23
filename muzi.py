# inkapulatsiya
from uuid import uuid4


class Avto:
    num_avto = 0
    """ Avtomabil klassi """
    def __init__(self, make, model, rang, yil, narx, km=0):
        self.make = make 
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        self.num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            return "Mashina km ini kamaytirib bolmaydi"


# avtomobil km: 1000
avto1 = Avto("GM", "Malibu", "qora", "2023", 3500000000)
avto2 = Avto("GM", "Gentra", "qora", "2023", 3500000000)


# print(f"Avtomobil km: {avto1.get_km()}km")
# print(f"Avtomobil id raqami: {avto1.get_id()}")
avto1.add_km(1000)
print(avto1.num_avto)
print(avto2.num_avto)
print(Avto.num_avto)
print(f"Avtomobil km: {avto1.get_km()}km ")