class Hero:
    
    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
 
    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name )
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

lesley = Hero('lesley', 100, 10, 5)
alucard = Hero('alucard', 100, 20, 10)

lesley.serang(alucard)
print("\n")
alucard.serang(lesley)
print("\n")
alucard.serang(lesley)
print("\n")
alucard.serang(lesley)
print("\n")
alucard.serang(lesley)
print("\n")
alucard.serang(lesley)