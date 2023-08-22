class Client():
    def __init__(self, tnumber, fio, schet, tarif):
        self.tnumber = tnumber
        self.fio = fio
        self.schet = schet
        self.tarif = tarif
        
class Company():
    def __init__(self):
        self.company = []
        
    def addClient(self, client):
        self.company.append(client)
    
    def showAll(self):
        for i in self.company:
            print(i.tnumber, i.fio, i.schet, i.tarif)
    
    def showClientByNumber(self, tnum):
        for t in self.company:
            if t.tnumber == tnum:
                print(t.tnumber, t.fio, t.schet, t.tarif)
                
    def showClientByFIO(self, f_i_o):
        for t in self.company:
            if t.fio == f_i_o:
                print(t.tnumber, t.fio, t.schet, t.tarif)
                
    def showClientsLower(self, money):
        for t in self.company:
            if t.schet < money:
                print(t.tnumber, t.fio, t.schet, t.tarif)
    
    def showClientsByTarif(self, tar):
        for t in self.company:
            if t.tarif == tar:
                print(t.tnumber, t.fio, t.schet, t.tarif)    

com = Company()
c1 = Client(88005553535, "Putin Vladimir Vladimirovich", 1000000000000000000, "GodMode")
com.addClient(c1)
com.showAll()
com.showClientByNumber(int(input("Number ")))
com.showClientByFIO(input("FIO "))
com.showClientsLower(int(input("Balanse lower ")))
com.showClientsByTarif(input("Tarif "))