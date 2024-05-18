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
print(inson.get_info())
print(f"{inson.get_age(2024)} yoshida")