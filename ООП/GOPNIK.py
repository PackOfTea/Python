class Gopnik():
    def __init__(self, name):
        
        self.hp = 100
        self.hit = 10
        self.name = name
        self.crit = 27
        self.intelekt = 10
        self.skill = "Пивка для рывка"
        self.skill2 = "Безстрашие"
        self.shmot = "Адик, пума и найки"
        self.regen = 15
        self.mana = 100
        
    def hit_it(self, any_punch):
        any_punch.hp -= self.hit
    def othil (self):
        if self.mana > 40:
            self.hp += self.regen
            self.mana -= 40           
        
            
pac = Gopnik("Maga228")
nepac = Gopnik("Mysor")

pac.hit_it(nepac)
print("HP:", nepac.hp)

nepac.othil()
nepac.othil()
nepac.othil()


print("Хэпэшечки:", pac.hp)
print("HP:", nepac.hp)
print("MANA", nepac.mana)