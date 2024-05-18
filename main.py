class Talaba:
    def __init__(self, ism, familya, t_yil, kurs):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.kurs = kurs  
          
    def get_name(self):
        return self.ism

    def get_age(self):
        yosh = 2024 - self.t_yil
        return yosh
    def get_kurs(self):
        return self.kurs

    
    def tanshitir(self):
        return f"ismim {self.ism} {self.familya}, tugilgan yilim {self.t_yil}"


talaba2 = Talaba("Teshmat", "Toshmat", 2000, 3)

print(talaba2.tanshitir())
print(talaba2.get_name())
print(talaba2.get_age())
print(talaba2.get_kurs())
