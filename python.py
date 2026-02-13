# class Doktor:
#     def __init__(self,name):
#         self.name=name
#         self.bemorlar=[]
#     def add_bemor(self,bemor_name):
#         self.bemorlar.append(bemor_name)

#     def show_bemor(self):
#         return self.bemorlar
#     def count_bemor(self):
#         return len(self.bemorlar)

# class Shifaxona:
#     def __init__(self,name):
#         self.name=name
#         self.doktorlar=[]
    
#     def add_doktor(self,doc_name):
#         self.doktorlar.append(doc_name)
#     def Show_doktor(self):
#         for index,ism in enumerate(self.doktorlar):
#             print(f"{index}.{ism}")
# class bemor:
#     def __init__(self,name):
#         self.name=name
    
#     def choose_doktor(self,doktor):
#         doktor.add_bemor(self.name)
#         print(f"{self.name} {doktor.name} ga navbatga yozildingiz")
#         print(f"navbatda : {doktor.count_bemor()}")


# bemor1=bemor("Abduvaid")
# bemor2=bemor("Ixlosbek")
# bemor3=bemor("Bdumajit")
# Doktor1=Doktor("DR Jamshid")
# Doktor2=Doktor("DR humoyun")
# Shifaxona=Shifaxona("1-son markaziy paliklinika")
# Shifaxona.add_doktor(Doktor1)
# Shifaxona.add_doktor(Doktor2)
# bemor1.choose_doktor(Doktor1)
# bemor2.choose_doktor(Doktor2)
# bemor3.choose_doktor(Doktor1)

class Avtomobil:
    def init(self , avto_nomi , avto_narx):
        self.avto_nomi = avto_nomi
        self.avto_narx = avto_narx
        self.mijozlar = []
    def add_mijoz(self , mijoz_name):
            self.mijozlar.append(mijoz_name)
    def narx_hisobla(self):
        return f'{self.avto_narx / 2}'
    def mijozlarni_korsatish(self):
        return self.mijozlar
    def navbat_mijozlar(self):
        return len(self.mijozlar)
    
class Avtosalon:
    def init(self , salon_name):
        self.salon_name = salon_name
        self.avtolar = []
    def add_avtomobil(self , avto_name):
        self.avtolar.append(avto_name)
    def avtolarni_korsatish(self): 
        for joylashuv , model in enumerate(self.avtolar):
            print(f'{joylashuv}.{model}')

class Haridor:
    def init(self, mijoz_ism):
        self.mijoz_ism = mijoz_ism
    def avto_tanlash(self , mashina):
        mashina.add_mijoz(self.mijoz_ism)
        print(f'{self.mijoz_ism} {mashina.avto_nomi} ga {mashina.narx_hisobla()}som tolab navbatga yozildi')
        print(f'Navbatda: {mashina.navbat_mijozlar()} nafar haridor bor.')


haridor1 = Haridor('Ixlosbek')
haridor2 = Haridor('Abduvaid')
avto1 = Avtomobil('jenytra.' , 160000000)
avto2 =Avtomobil('cobalt' , 150000000)
avtosalon1 = Avtosalon('Pitnak bozor')
avtosalon1.add_avtomobil(avto1)
avtosalon1.add_avtomobil(avto2)
haridor1.avto_tanlash(avto1)
