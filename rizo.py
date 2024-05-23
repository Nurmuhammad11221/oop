# 1
# class Shaxs:
#     def __init__(self, ism, familya, t_yil, passport):
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil
#         self.passport = passport

#     def get_age(self):
#         yosh = 2024 - self.t_yil
#         return yosh

#     def get_familya(self):
#         return self.familya

#     def get_passport(self):
#         return self.passport

# inson = Shaxs("Teshmat", "Boltavoyev", 2000, "AC1003243")

# print(inson.get_age())
# print(inson.get_familya())
# print(inson.get_passport())

 # 2        


class Shaxs:
    def __init__(self, ism, familya, passport, t_yil):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.passport = passport
        
    def get_info(self):
        info = f"{self.ism} {self.familya}\n"
        info += f"{self.passport}, {self.t_yil}-yilda tugilgan"
        return info
    def get_age(self, yil):
        age = yil - self.t_yil
        return age

inson = Shaxs("Teshmat", "Boltavoyev", "AC1003243", 2000)
# print(inson.get_info())
# print(f"{inson.get_age(2024)} yoshida")


class Talaba(Shaxs):
    """ Talaba klasi """
    def __init__(self, ism, familya, passport, t_yil, IDraqam, manzil):
        super().__init__(ism, familya, passport, t_yil)
        self.IDraqam = IDraqam
        self.bosqich = 1
        self.manzil = manzil
            

    def get_id(self):
        """ Talabning id raqam """
        return self.IDraqam
    def get_bosqich(self):
        """ Talabning nechinchi kursligi """
        return self.bosqich
    def get_info(self):
        info = f"{self.ism} {self.familya}\n"
        info += f"{self.get_bosqich()}- bosqich talabasi, talaba id: #{self.get_id()}"
        return info

# talaba = Talaba("BOltavoyev", "teshaboy", "AC1003243", 2020, "5198733")

# print(talaba.get_info())
# print(talaba.get_id())

class Manzil:
    def __init__(self, uy, kocha, tuman, shaxar):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.shaxar = shaxar
        
    def get_manzil(self):
        """ Manzilni korish """
        manzil = f"{self.shaxar}, {self.tuman} tumani,\n"
        manzil += f"{self.kocha}, {self.uy}-uy"
        return manzil
        
talaba_manzil = Manzil(28, "nur", "uchtepa", "tosheknt")
talaba = Talaba("BOltavoyev", "teshaboy", "AC1003243", 2020, "5198733", talaba_manzil)
print(talaba_manzil.get_manzil())
print(talaba_manzil.tuman)


class Fan:
    def __init__(self,nomi):
        self.nomi = nomi

    def get_name(self):
        return self.nomi
        