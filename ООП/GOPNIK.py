class Gopnik():
    def __init__(self, name):
        
        self.hp = 100
        self.hit = 10
        self.name = name
        self.crit = 27
        self.intelekt = 10
        self.skill = "����� ��� �����"
        self.skill2 = "����������"
        self.shmot = "����, ���� � �����"
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


print("���������:", pac.hp)
print("HP:", nepac.hp)
print("MANA", nepac.mana)