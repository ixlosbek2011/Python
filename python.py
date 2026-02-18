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

# class Avtomobil:
#     def init(self , avto_nomi , avto_narx):
#         self.avto_nomi = avto_nomi
#         self.avto_narx = avto_narx
#         self.mijozlar = []
#     def add_mijoz(self , mijoz_name):
#             self.mijozlar.append(mijoz_name)
#     def narx_hisobla(self):
#         return f'{self.avto_narx / 2}'
#     def mijozlarni_korsatish(self):
#         return self.mijozlar
#     def navbat_mijozlar(self):
#         return len(self.mijozlar)
    
# class Avtosalon:
#     def init(self , salon_name):
#         self.salon_name = salon_name
#         self.avtolar = []
#     def add_avtomobil(self , avto_name):
#         self.avtolar.append(avto_name)
#     def avtolarni_korsatish(self): 
#         for joylashuv , model in enumerate(self.avtolar):
#             print(f'{joylashuv}.{model}')

# class Haridor:
#     def init(self, mijoz_ism):
#         self.mijoz_ism = mijoz_ism
#     def avto_tanlash(self , mashina):
#         mashina.add_mijoz(self.mijoz_ism)
#         print(f'{self.mijoz_ism} {mashina.avto_nomi} ga {mashina.narx_hisobla()}som tolab navbatga yozildi')
#         print(f'Navbatda: {mashina.navbat_mijozlar()} nafar haridor bor.')


# haridor1 = Haridor('Ixlosbek')
# haridor2 = Haridor('Abduvaid')
# avto1 = Avtomobil('jenytra.' , 160000000)
# avto2 =Avtomobil('cobalt' , 150000000)
# avtosalon1 = Avtosalon('Pitnak bozor')
# avtosalon1.add_avtomobil(avto1)
# avtosalon1.add_avtomobil(avto2)
# haridor1.avto_tanlash(avto1)

# class Poyezd:
#     def __init__(self,qayerdan,qayerga,narx):
#         self.qayerdan=qayerdan
#         self.qayerga=qayerga
#         self.narx=narx
#     def malumot (self):
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

# class Avtomobil:
#     def init(self , avto_nomi , avto_narx):
#         self.avto_nomi = avto_nomi
#         self.avto_narx = avto_narx
#         self.mijozlar = []
#     def add_mijoz(self , mijoz_name):
#             self.mijozlar.append(mijoz_name)
#     def narx_hisobla(self):
#         return f'{self.avto_narx / 2}'
#     def mijozlarni_korsatish(self):
#         return self.mijozlar
#     def navbat_mijozlar(self):
#         return len(self.mijozlar)
    
# class Avtosalon:
#     def init(self , salon_name):
#         self.salon_name = salon_name
#         self.avtolar = []
#     def add_avtomobil(self , avto_name):
#         self.avtolar.append(avto_name)
#     def avtolarni_korsatish(self): 
#         for joylashuv , model in enumerate(self.avtolar):
#             print(f'{joylashuv}.{model}')

# class Haridor:
#     def init(self, mijoz_ism):
#         self.mijoz_ism = mijoz_ism
#     def avto_tanlash(self , mashina):
#         mashina.add_mijoz(self.mijoz_ism)
#         print(f'{self.mijoz_ism} {mashina.avto_nomi} ga {mashina.narx_hisobla()}som tolab navbatga yozildi')
#         print(f'Navbatda: {mashina.navbat_mijozlar()} nafar haridor bor.')


# haridor1 = Haridor('Ixlosbek')
# haridor2 = Haridor('Abduvaid')
# avto1 = Avtomobil('jenytra.' , 160000000)
# avto2 =Avtomobil('cobalt' , 150000000)
# avtosalon1 = Avtosalon('Pitnak bozor')
# avtosalon1.add_avtomobil(avto1)
# avtosalon1.add_avtomobil(avto2)
# haridor1.avto_tanlash(avto1)



# class Ovqat:
#     def init(self, ovqat_nomi, ovqat_narxi):
#         self.ovqat_nomi = ovqat_nomi
#         self.ovqat_narxi = ovqat_narxi
#         self.mijozlar = []

#     def add_mijoz(self, mijoz_ismi):
#         self.mijozlar.append(mijoz_ismi)


# class Restoran:
#     def init(self, restoran_nomi):
#         self.restoran_nomi = restoran_nomi
#         self.ovqatlar = []

#     def add_food(self, food_name):
#         self.ovqatlar.append(food_name)


# class Mijoz:
#     def init(self, klient_name):
#         self.klient_name = klient_name
#         self.jami_summa = 0  
#     def ovqat_tanlash(self, food, soni):
#         food.add_mijoz(self.klient_name)
#         narx = food.ovqat_narxi * soni
#         self.jami_summa += narx 
#         print(f"{self.klient_name} {soni}ta {food.ovqat_nomi} buyurtma qildi {narx} so'm")
#     def jami_hisob(self):
#         print(f"UMUMIY XISOB: {self.jami_summa}som")



# mijoz1 = Mijoz('Ali')

# ovqat1 = Ovqat('Shashlik', 16000)
# ovqat2 = Ovqat('Suv', 15000)
# ovqat3 = Ovqat('Salad', 55000)
# ovqat4 = Ovqat('Sansebastian', 50000)
# mijoz1.ovqat_tanlash(ovqat1, 4)
# mijoz1.ovqat_tanlash(ovqat2, 2)
# mijoz1.ovqat_tanlash(ovqat3, 2)
# mijoz1.ovqat_tanlash(ovqat4, 1)

# mijoz1.jami_hisob()
class Poyezd:
    def __init__(self, qayerdan, qayerga, narx, yoshingiz):
        self.qayerdan = qayerdan
        self.qayerga = qayerga
        self.narx = narx
        self.yoshingiz = yoshingiz

    def malumot_ber(self):
        return f"sizning chiptangiz: {self.qayerdan} dan {self.qayerga} ga yoshingiz {self.yoshingiz} chipta narxi {self.narx}"


class Vagon(Poyezd):
    def __init__(self, qayerdan, qayerga, narx, yoshingiz, vagon_turi):
        super().__init__(qayerdan, qayerga, narx, yoshingiz)
        self.vagon_turi = vagon_turi

    def chipta_narxi(self):
        if self.yoshingiz < 5:
            return "siz uchun chipta bepul"
        else:
            return f"Chipta narxi: {self.narx}"

    def malumot_ber(self):  
        return (f"Sizning chiptangiz: {self.qayerdan} dan {self.qayerga} ga "
                f"yoshingiz {self.yoshingiz}, vagon turi {self.vagon_turi} "
                f"{self.chipta_narxi()}")


vagon1 = Vagon("Toshkent", "America", "400$", 15, "Lux")

print(vagon1.malumot_ber())
