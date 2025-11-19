                                # 1
# class Talaba:
#     def __init__(self, ismi, kursi):
#         self.ismi = ismi
#         self.kursi = kursi
#         self.talaba_soni = 0
#         self.talabalar = []

#     def malumotlar(self):
#         return f"{self.ismi}, {self.kursi}"

#     def add_talaba(self, ismi, kursi):
#         oquvchi = Talaba(ismi, kursi)
#         self.talabalar.append(oquvchi)
#         self.talaba_soni += 1

#     def malumot_ber(self):
#         return f"Talaba ismi: {self.ismi}, u {self.kursi}-kursda oqiydi"
# talaba_1 = Talaba('Ixlosbek', 2)
# print(talaba_1.malumot_ber())
                                # 2
# class mashina:
#     def __init__(self,madeli,rangi,yili):
#         self.madeli=madeli
#         self.rangi=rangi
#         self.yili=yili
#         self.mashina_soni=0
#         self.mashinalar=[]
#     def malumotlar(self):
#         return f"{self.madeli},{self.rangi},{self.yili}"
#     def add_mashina(self,madeli,rangi,yili):
#         moshin=mashina(madeli,rangi,yili)
#         self.mashinalar.append(moshin)
#         self.mashina_soni+=1
#     def malumot_ber(self):
#         return f"{self.madeli}  mashinasi rangi {self.rangi} yili  {self.yili}"
# moshina_1=mashina('damas',"oq",2025)
# print(moshina_1.malumot_ber())
#                                     # 3
# import math
# class doira:
#     def __init__(self,radius):
#         self.radius=radius

#     def yuza_hisobla(self):
#         s=math.pi * math.pow(self.radius,2)
#         return f"{self.radius} li doira yuzi {s} ga teng"
#     def uzinlik_hisoba(self):
#         L = 2 * math * self.radius
#         return f"{self.radius} li doira uzunlugiga teng"
# doira=doira(5)
# print(doira.yuza_hisobla(), doira.uzinlik_hisoba())
# class hisoblash:
#     def __init__(self,qoshish ,ayirish):
#         self.qoshish=qoshish
#         self.ayirish=ayirish
#         self.hisobla=0
#         self.hisoblashlar=[]
#     def malumotlar(self):
#         return f"{self.qoshish}+{self.ayirish}"
#     def add_hisob(self,qoshish,ayirish):
#         hisob=hisoblash(qoshish,ayirish)
#         hisoblashlar.append(hisob)
#         self.hisobla+=1
#     def malumot_ber(self):
#         return({self.qoshish}+{self.ayirish})
# hisoblash_1=hisoblash(45,25) 
# print(hisoblash_1.malumot_ber())
                                    # 5
# class talaba:
#     def __init__(self,baxosi):

#          self.baxosi=baxosi
#     def malumotlar(self,yangi_baxo):
#         self.yangi_baxo=yangi_baxo
#         self.baxosi=yangi_baxo
#     def malumot_ber(self):
#         return f"{self.baxosi}-oquvchining baxosi"
# baxo1=talaba(4)
# baxo1.yangi_baxo
# print(baxo1.malumot_ber())
# class ishchi:
#     def __init__(slef,soati,kechgi,kuni,oyligi):
#         self.kuni=kuni
#         self.oyligi=oyligi
#         self.soati=soati
#         self.kechgi=kechgi
#     def oylik(sslf):
#         return f"{self.kuni*self.oyligi}ishchining kunlik oyligi"
# ishchi_1=ishchi(200,6000)
# print(ishchi_1.oylik)

# class kitob:
#     def __init__(self,sarlavha,muallif,sahifa):
#         self.sarlavha=sarlavha
#         self.muallif=muallif
#         self.sahifa=sahifa
#     def malumotlar(self):
#         return f"{self.sarlavha},{self.muallif},{self.sahifa}"
# class kampyuter:
#     def __init__(self,ram,hdd,cpu):
#         self.ram=ram
#         self.hdd=hdd
#         self.cpu=cpu
#         self.kompyutur=0
#         self.list=[]
#     def malumot(self):
#         return f"{self.ram}{self.hdd}{self.cpu}"
#     def info(self,ram,hdd,cpu):
#         kamp=kampyuter(ram,hdd,cpu)
#         self.list.append(kamp)
#         self.kompyutur+=1
#     def malumot_ber(self):
#         return f"kampyutur ram {self.ram}; HDD {self.hdd}; cpu  {self.cpu};"
# kampyuter_1=kampyuter("46f4df4s4f6","46444464466","55684646464444444")
# print(kampyuter_1.malumot_ber())

# class oquvchilar:
#     def __init__(self,oquvchilar):
#         self.oquvchilar=oquvchilar
#         self.oquv=0
#         self.list=[]
#     def malumot(self):
#         return f"{self.oquvchilar}"
#     def info (self,oquvchilar):
#         oquvchi=oquvchilar(oquvchilar)
#         list.append(oquvchi)
#         oquv+=1
#     def malumot_ber(self):
#         return f"8-son maktabining 8-A sinf o`quvchisi{self.oquvchilar}"
# talaba_1=oquvchilar("muxtorov ixlosbek")
# talaba_2=oquvchilar("jonibekov azamat")
# print(talaba_1.malumot_ber())
# print(talaba_2.malumot_ber())
# from pickle import APPEND


# class tanishuv:
#     def __init__(self,shaxs):
#         self.shaxs=shaxs
#         self.shaxslar=0
#         self.list=[]
#     def malumot(self):
#         return f"{self.shaxs}"
#     def info(self,shaxs):
#         tanish=tanishuv(shaxs)
#         list.append(tanish)
#         self.shaxslar+=1
#     def malumot_ber(self):
#         return f"shaxs malumotlari ismi sharifi {self.shaxs}"
# talaba_1=tanishuv("muxtorov ixllkosbek")
# print(talaba_1.malumot_ber())


# class maktab:
#     def __init__(self,maktabi,sinfi):
#         self.maktabi=maktabi
#         self.sinfi=sinfi
#         self.soni=0
#         self.list=[]
#     def malumot(self):
#         return f"talabaning maktabi {self.maktabi}i ning {self.self} sinifida oqiydi"
#     def info(self,maktabi,sinfi):
#         mk=maktab(maktabi,sinfi)
#         list.append(mk)
#         soni+=1
#     def malumot_ber(self):
#         return f"talabaning maktabi {self.maktabi}i ning {self.self} sinifida oqiydi"
# talaba_1=maktab('8-son maktabi','8-A')
# print(talaba_1.malumot_ber())
# class Bola:
#     def init(self ,sharif):
#         self.sharif=sharif
#     def malumot(self):
#         return f"{self.sharif}-oquvchining ismi {self.yosh}-yoshda"

# class Sinf:
#     def init(self ,sinf ,yosh):
#         self.sinf=sinf
#         self.yosh=yosh
#         self.royhat=[]
#     def oquvchi_qosh(self ,sharif):
#         student=Bola(sharif)
#         self.royhat.append(student)
#         if self.yosh==14:
#             return f"{self,sharif}-oquvchi {self.sinf}-ga boradi"
#         elif self.yosh==15:
#             return f"{self,sharif}-oquvchi {self.sinf}-ga boradi"
#         elif self.yosh==16:
#             return f"{self,sharif}-oquvchi {self.sinf}-ga boradi"
#         elif self.yosh==17:
#             return f"{self,sharif}-oquvchi {self.sinf}-ga boradi"
#         elif self.yosh==18:
#             return f"{self,sharif}-oquvchi {self.sinf}-ga boradi"
#         else:
#             return "O'quvchi maktabni bitirgan"
#     def final(self):
#         oquvchi="".join([i.malumot() for i in self.royhat])
#         return f"{oquvchi}"
# talaba1=Sinf(8 ,14)
# talaba1.oquvchi_qosh("Abdumajid Xudayberganov")
# print(talaba1.final())

#13
# class Kitob:
#     def init(self ,nom ,mualif ,sahifa):
#         self.nomi=nom
#         self.mualif=mualif
#         self.sahifa=sahifa
#     def malumot(self):
#         return f"{self.nomi}-kitob nomi {self.mualif}-kitobni yozgan odam ,{self.sahifa}-kitob sahifasi"
# class Kutubxona:
#     def init(self ,addres):
#         self.adres=addres
#         self.royhat=[]
#     def kitob_qosh(self ,nom ,mualif ,sahifa):
#         haqida=Kitob(nom ,mualif ,sahifa)
#         self.royhat.append(haqida)
#     def final(self):
#         ktob="".join([i.malumot() for i in self.royhat])
#         return f"{self.adres}-bastalangan ,{ktob}"
# kitob1=Kutubxona("Mustaqillik kochasida Toshkent viloyatida")
# kitob1.kitob_qosh("Al-jabr" ,"Al-Xorazmiy" ,800)
# print(kitob1.final())
# class kamponiya:
#     def __init__(self,kampon):
#         self.kampon=kampon
#     def malumot (self):
#         return f"{self.kampon}"
# class ishchi:
#     def __init__(self,ishchilar):
#         self.ishchilar=ishchilar
#         self.soni=0
#         self.list=[]
#     def malum(self,kampon):
#         ishchi=kamponiya(kampon)
#         self.list.append(ishchi)
#         self.soni+=1
#     def malumot_ber(self):
#         return f"{self.kamon} kamponiyasida {self.ishchilar} ishlaydi"
# ish_1=ishchi('ixlosbek muxtorov')
# ish_1.malum("it park")
# print(ish_1.malumot_ber())


# import re


# class Talaba:
#     def __init__(self,ismi,yoshi):
#         self.ism = ismi
#         self.yosh = yoshi
#     def get_info(self):
#         return f"Talaba ismi : {self.ism} , talaba yoshi : {self.yosh}"

# class Universitet(Talaba):
#     def __init__(self, ismi, yoshi,bahosi):
#         super().__init__(ismi, yoshi)   
#         self.baho = bahosi
#     def get_info(self):
#         return f"{Talaba.get_info(self)} talaba bahosi: {self.baho}"

    
# talaba1 = Universitet("Nizomjon" , 15 ,2)
# print(talaba1.get_info())
    
# ismlar = ["ali","vali","asad","amin","asqar"]

# name  = "\n".join([ism for ism in ismlar if ism.startswith("s")])
# print(name)
# print([ism for ism in ismlar if ism.startswith("a")])
# a_bilan_boshlanganlar = []
# for ism in ismlar:
#     if ism.startswith("a"):
#         a_bilan_boshlanganlar.append(ism)

# print(a_bilan_boshlanganlar)

# def summaa(a,b):
#     return a + b

# print(summaa(10,20))

# summaa = lambda a,b : a**b
# print(summaa(10,20))
# 29
# class Oyinchi:
#     def init(self , nik , level , ball):
#         self.nik = nik
#         self.level = level
#         self.ball= ball
#     def malumot(self):
#         return f'Oyinchi: {self.nik}\nLevel: {self.level}\nBall: {self.ball}\n\n'
    
# class Oyin:
#     def init(self,  nomi):
#         self.nomi= nomi
#         self.royhat= []
#     def add_gamer(self, nik , level , ball):
#         oyinchi = Oyinchi(nik , level , ball)
#         self.royhat.append(oyinchi)
#     def info(self):
#         gamer = '\n'.join([i.malumot() for i in self.royhat])
#         return  f'{self.nomi} oyinini oynaydigan oyinchilar: \n{gamer}\n'
    
# oyin1 = Oyin('CS2')
# oyin1.add_gamer('Pirate' , 82 , 93)
# print(oyin1.info())

                                                                                # 30
# class Taom:
#     def init(self ,nomi , narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#     def malumot(self):
#         return f'{self.nomi} , {self.narxi}so\'m'

# class Restoran:
#     def init(self , res_nomi):
#         self.res_nomi = res_nomi
#         self.royhat = []
#     def add_food(self, nomi , narxi):
#         taom = Taom(nomi , narxi)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.res_nomi} restorani menyusi: \n{food}\n'

# restoran1 = Restoran('Gavhar')
# restoran1.add_food('Tuxum barak' ,'40000')
# restoran1.add_food('Go\'mma',  '35000')
# print(restoran1.info())



                                                                        #     31
# class Taom:
#     def init(self, nom , narx  , kaloriya):
#         self.nom=  nom
#         self.narx = narx
#         self.kaloriya = kaloriya
#     def malumot(self):
#         return f'{self.nom} , narxi {self.narx}so\'m'
    
# class Taom_qosh:
#     def init(self):
#         self.royhat = []
#     def add_food(self , nom , narx  , kaloriya):
#         taom = Taom(nom , narx  , kaloriya)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\n{food}\n'
    
# food1 = Taom_qosh()
# food1.add_food('Tuxum barak' , 40000 , 700)
# food1.add_food('Palov' , 35000 , 600)
# print(food1.info())


                                                    # 32
# class Taom:
#     def init(self, nom , narx  , kaloriya):
#         self.nom=  nom
#         self.narx = narx
#         self.kaloriya = kaloriya
#     def malumot(self):
#         return f'{self.nom} , narxi {self.narx}so\'m , Kaloriya: {self.kaloriya}'
    
# class Restoran:
#     def init(self , nomi , manzil):    
#         self.nomi = nomi
#         self.manzil = manzil
#         self.royhat = []
#     def add_food(self ,  nom , narx  , kaloriya):
#         taom = Taom( nom , narx  , kaloriya)
#         self.royhat.append(taom)
#     def info(self):
#         food = '\n'.join([i.malumot() for i in self.royhat])
#         return f'{self.nomi} Reastoran menyusi ({self.manzil}da joylashgan): \n{food}\n'

# restoran1 = Restoran('Gavhar' , 'Urganch shaxri')
# restoran1.add_food('Palov' , 45000 , 600)
# print(restoran1.info())


                                                            # 33
# class Dastur:
#     def init(self,  nomi ):
#         self.nomi = nomi
#     def malumot(self):
#         return f'{self.nomi}'
    
# class Kompyuter:
#     def init(self):
#         self.royhat = []
#     def add_programming(self , nomi):
#         dastur = Dastur(nomi)
#         self.royhat.append(dastur)
#     def info(self):
#         programma = '\n'.join([i.malumot() for i in self.royhat])
#         return f'Kompyuterdagi dasturlar: \n{programma}\n'
    
# komp1 = Kompyuter()
# komp1.add_programming('Visual Studio Code')
# komp1.add_programming('Chrome')
# komp1.add_programming('Telegram')
# print(komp1.info())
# 34
# class Dastur:
#     def init(self , nomi , versiya , ishlab_chiqaruvchi):
#         self.nomi = nomi
#         self.versiya = versiya
#         self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
#     def malumot(self):
#         return f'{self.nomi} , {self.versiya} versiyada , {self.ishlab_chiqaruvchi} ishlab chiqargan'

# class Dastur_qosh:
#     def init(self):
#         self.royhat = []
#     def add_programming(self , nomi , versiya , ishlab_chiqaruvchi):
#         dastur = Dastur(nomi , versiya , ishlab_chiqaruvchi)
#         self.royhat.append(dastur)
#     def info(self):
#         programma = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\n{programma}\n'
    
# dastur1 = Dastur_qosh()
# dastur1.
# class bank :
#     def __init__(self,mijozlar):
#         self.mijozlar=mijozlar
#         self.odamlar=0
#         self.list=[]
#     def malumot(self):
#         return f"{self.mijozlar}"
#     def get_info(self,mijozlar):
#         mijoz=bank(mijozlar)
#         self.list.append(mijoz)
#         self.odamlar+=1
#     def malumt_ber(self):
#         return f"{self.mijozlar}"
# bank_1=bank("")
# class Mijoz:
#     def init(self, ism , familiya , balans):
#         self.ism = ism
#         self.familiya = familiya
#         self.balans = balans
#     def malumot(self):
#         return f'{self.familiya} {self.ism} , balansida {self.balans}$ miqdorida pul bor'
    
# class Bank:
#     def init(self , nomi , yili , mijozlar_soni):
#         self.nomi = nomi
#         self.yili = yili
#         self.mijozlar_soni = mijozlar_soni
#         self.royhat = []
#     def bank_haqida(self):
#         return f'\t{self.nomi} , {self.yili}dan beri ishlab kelmoqda , shu kungacha {self.mijozlar_soni}mln dan ortiq mijoz bu bankdan foydanangan.'
#     def add_mijoz(self , ism , familiya , balans):
#         mijoz = Mijoz(ism , familiya , balans)
#         self.royhat.append(mijoz)
#     def del_mijoz(self , ism , familiya , balans ):
#         return f'\t\tBankdagi ishini yakunlagan mijozlar:\n{ism} {familiya}  , balansida {balans}$ miqdorida pul bor.'

#     def info(self):
#         klient = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\t\t{self.nomi} dan hozirda foydalanyotgan mijozlar \n{klient}\n'
    
# bank1 = Bank('Agrobank' , 1977 , 30)
# bank1.add_mijoz('Ali' , 'Aliyev' , 430)
# bank1.add_mijoz('Vali',  'Valiyev' , 810)

# print(bank1.info())
# print(bank1.del_mijoz('Ali' , 'Aliyev' , 430))
# print(bank1.bank_haqida())

                                # 36

# class Mijoz:
#     def init(self , ism , familiya ,  balans):
#         self.ism = ism
#         self.familiya = familiya
#         self.balans = balans
#     def info(self):
#         return f'{self.familiya} {self.ism} , balansida {self.balans}$ pul bor'
    
# mijoz1 = Mijoz('Ali' , 'Aliev' , 270)
# print(mijoz1.info())



                                                                    # 37
# class Fan:
#     def init(self , nomi):
#         self.nomi= nomi
#     def malumot(self):
#         return f'{self.nomi}'

# class Sinf:
#     def init(self , sinf):
#         self.sinf = sinf
#         self.royhat = []
#     def add_fan(self , nomi):
#         fan = Fan(nomi)
#         self.royhat.append(fan)
#     def info(self):
        # clas = '\n'.join([i.malumot() for i in self.royhat]) 
        # return f'{self.sinf} sinfidagi fanlar royhati: \n{clas}\n'
    
# sinf1 = Sinf('8-B')
# sinf1.add_fan('Algebra')
# sinf1.add_fan('Fizika')
# print(sinf1.info())


                                                                        # 38
# class Fan:
#     def init(self , nom , oqituvchi):
#         self.nom = nom
#         self.oqituvchi = oqituvchi
#     def info(self):
#         return f'{self.nom} fanidan {self.oqituvchi} dars beradi'

# fan1 = Fan('Dasturlash' , 'Xusainov Mirzabek')
# print(fan1.info())

# 39
# class Talaba:
#     def init(self , ism , familiya , kurs):
#         self.ism = ism
#         self.familiya = familiya
#         self.kurs = kurs
#     def talaba_malumot(self):
#         return f'{self.familiya} {self.ism} , {self.kurs} kursda oqiydi'
    
# class Oqituvchi:
#     def init(self , ismi , familiyasi , fan):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.fan = fan
#     def oqituvchi_malumot(self):
#         return f'{self.familiyasi} {self.ismi} , {self.fan} fanidan dars beradi'
    
# class Universitet:
#     def init(self , nomi):
#         self.nomi = nomi
#         self.talaba_royhat = []
#         self.oqituvchi_royhat = []
#         self.oqituvchilar_soni = 0
#     def add_student(self , ism , familiya , kurs):
#         talaba = Talaba(ism , familiya , kurs)
#         self.talaba_royhat.append(talaba)
#     def add_teacher(self , ismi , familiyasi , fan):
#         oqituvchi = Oqituvchi(ismi , familiyasi , fan)
#         self.oqituvchi_royhat.append(oqituvchi)
#         self.oqituvchilar_soni +=1
#     def talaba_info(self):
#         student = "\n".join([i.talaba_malumot() for i in self.talaba_royhat])
#         return f'{self.nomi} nomli universitetda talim oladigan talabalar: \n{student}\n'
#     def teacher_info(self):
#         teacher = '\n'.join([n.oqituvchi_malumot() for n in self.oqituvchi_royhat])
#         return f'{self.nomi} nomli universitetda {self.oqituvchilar_soni}ta oqituvchi talim beradi va ular: \n{teacher}\n'
    
# univer1 = Universitet('UrDU')
# univer1.add_teacher('Ali' , 'Aliyev' , 'Iqsodiyot')
# univer1.add_student('Vali' , 'Valiyev' , 1)
# print(univer1.teacher_info())
# print(univer1.talaba_info())



                                                                                # 40
# class Mijoz:
#     def init(self , ismi):
#         self.ismi = ismi
#     def mijoz_malumot(self):
#         return f'{self.ismi}'
# class Maxsulot:
#     def init(self , nomi , narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#     def maxsulot_malumot(self):
#         return f'{self.nomi} , narxi {self.narxi}so\'m'

# class Dokon:
#     def init(self , dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.mijoz_royhat =  []
#         self.maxsulot_royhat = []
#     def add_product(self , nomi , narxi ):
#         maxsulot = Maxsulot(nomi , narxi)
#         self.maxsulot_royhat.append(maxsulot)
#     def add_mijoz(self , ismi):
#         mijoz = Mijoz(ismi)
#         self.mijoz_royhat.append(mijoz)
#     def maxsulot_info(self):
#         product = "\n".join([i.maxsulot_malumot() for i in self.maxsulot_royhat])
#         return f'{self.dokon_nomi} nomli dokondagi maxsulotlar: \n{product}\n'
#     def mijoz_info(self):
#         odam = ''.join([n.mijoz_malumot() for n in self.mijoz_royhat])
#         return f'{self.dokon_nomi} nomli dokondagi mijozlar: \n{odam}\n'

# dokon1 = Dokon('Rustam aga')
# dokon1.add_product('Sut' , 14000)
# dokon1.add_mijoz('Ali')
# print(dokon1.maxsulot_info())
# print(dokon1.mijoz_info())
# class teatr:
#     def __init__(self,royhatlar):
#         self.royhatlar=royhatlar
#         self.soni=0
#         self.lis=[]
#     def malumot(self):
#         return f"{self.royhatlar}"
#     def add_teatr(self,royhatlar):
#         spek=teatr(royhatlar)
#         self.lis.append(spek)
#         self.soni+=1
#     def malumot_ber (self):
#         return f"{self.royhatlar} teartri"
# teatr_1=teatr('qogirchoqlar')
# print(teatr_1.malumot_ber())

# class Mijoz:
#     def init(self, ism , familiya , balans):
#         self.ism = ism
#         self.familiya = familiya
#         self.balans = balans
#     def malumot(self):
#         return f'{self.familiya} {self.ism} , balansida {self.balans}$ miqdorida pul bor'
    
# class Bank:
#     def init(self , nomi , yili , mijozlar_soni):
#         self.nomi = nomi
#         self.yili = yili
#         self.mijozlar_soni = mijozlar_soni
#         self.royhat = []
#     def bank_haqida(self):
#         return f'\t{self.nomi} , {self.yili}dan beri ishlab kelmoqda , shu kungacha {self.mijozlar_soni}mln dan ortiq mijoz bu bankdan foydanangan.'
#     def add_mijoz(self , ism , familiya , balans):
#         mijoz = Mijoz(ism , familiya , balans)
#         self.royhat.append(mijoz)
#     def del_mijoz(self , ism , familiya , balans ):
#         return f'\t\tBankdagi ishini yakunlagan mijozlar:\n{ism} {familiya}  , balansida {balans}$ miqdorida pul bor.'

#     def info(self):
#         klient = '\n'.join([i.malumot() for i in self.royhat])
#         return f'\t\t{self.nomi} dan hozirda foydalanyotgan mijozlar \n{klient}\n'
    
# bank1 = Bank('Agrobank' , 1977 , 30)
# bank1.add_mijoz('Ali' , 'Aliyev' , 430)
# bank1.add_mijoz('Vali',  'Valiyev' , 810)

# print(bank1.info())
# print(bank1.del_mijoz('Ali' , 'Aliyev' , 430))
# print(bank1.bank_haqida())

                                # 36

# class Mijoz:
#     def init(self , ism , familiya ,  balans):
#         self.ism = ism
#         self.familiya = familiya
#         self.balans = balans
#     def info(self):
#         return f'{self.familiya} {self.ism} , balansida {self.balans}$ pul bor'
    
# mijoz1 = Mijoz('Ali' , 'Aliev' , 270)
# print(mijoz1.info())



                                                                    # 37
# class Fan:
#     def init(self , nomi):
#         self.nomi= nomi
#     def malumot(self):
#         return f'{self.nomi}'

# class Sinf:
#     def init(self , sinf):
#         self.sinf = sinf
#         self.royhat = []
#     def add_fan(self , nomi):
#         fan = Fan(nomi)
#         self.royhat.append(fan)
#     def info(self):
        # clas = '\n'.join([i.malumot() for i in self.royhat]) 
        # return f'{self.sinf} sinfidagi fanlar royhati: \n{clas}\n'
    
# sinf1 = Sinf('8-B')
# sinf1.add_fan('Algebra')
# sinf1.add_fan('Fizika')
# print(sinf1.info())


                                                                        # 38
# class Fan:
#     def init(self , nom , oqituvchi):
#         self.nom = nom
#         self.oqituvchi = oqituvchi
#     def info(self):
#         return f'{self.nom} fanidan {self.oqituvchi} dars beradi'

# fan1 = Fan('Dasturlash' , 'Xusainov Mirzabek')
# print(fan1.info())

# 39
# class Talaba:
#     def init(self , ism , familiya , kurs):
#         self.ism = ism
#         self.familiya = familiya
#         self.kurs = kurs
#     def talaba_malumot(self):
#         return f'{self.familiya} {self.ism} , {self.kurs} kursda oqiydi'
    
# class Oqituvchi:
#     def init(self , ismi , familiyasi , fan):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.fan = fan
#     def oqituvchi_malumot(self):
#         return f'{self.familiyasi} {self.ismi} , {self.fan} fanidan dars beradi'
    
# class Universitet:
#     def init(self , nomi):
#         self.nomi = nomi
#         self.talaba_royhat = []
#         self.oqituvchi_royhat = []
#         self.oqituvchilar_soni = 0
#     def add_student(self , ism , familiya , kurs):
#         talaba = Talaba(ism , familiya , kurs)
#         self.talaba_royhat.append(talaba)
#     def add_teacher(self , ismi , familiyasi , fan):
#         oqituvchi = Oqituvchi(ismi , familiyasi , fan)
#         self.oqituvchi_royhat.append(oqituvchi)
#         self.oqituvchilar_soni +=1
#     def talaba_info(self):
#         student = "\n".join([i.talaba_malumot() for i in self.talaba_royhat])
#         return f'{self.nomi} nomli universitetda talim oladigan talabalar: \n{student}\n'
#     def teacher_info(self):
#         teacher = '\n'.join([n.oqituvchi_malumot() for n in self.oqituvchi_royhat])
#         return f'{self.nomi} nomli universitetda {self.oqituvchilar_soni}ta oqituvchi talim beradi va ular: \n{teacher}\n'
    
# univer1 = Universitet('UrDU')
# univer1.add_teacher('Ali' , 'Aliyev' , 'Iqsodiyot')
# univer1.add_student('Vali' , 'Valiyev' , 1)
# print(univer1.teacher_info())
# print(univer1.talaba_info())



                                                                                # 40
# class Mijoz:
#     def init(self , ismi):
#         self.ismi = ismi
#     def mijoz_malumot(self):
#         return f'{self.ismi}'
# class Maxsulot:
#     def init(self , nomi , narxi):
#         self.nomi = nomi
#         self.narxi = narxi
#     def maxsulot_malumot(self):
#         return f'{self.nomi} , narxi {self.narxi}so\'m'

# class Dokon:
#     def init(self , dokon_nomi):
#         self.dokon_nomi = dokon_nomi
#         self.mijoz_royhat =  []
#         self.maxsulot_royhat = []
#     def add_product(self , nomi , narxi ):
#         maxsulot = Maxsulot(nomi , narxi)
#         self.maxsulot_royhat.append(maxsulot)
#     def add_mijoz(self , ismi):
#         mijoz = Mijoz(ismi)
#         self.mijoz_royhat.append(mijoz)
#     def maxsulot_info(self):
#         product = "\n".join([i.maxsulot_malumot() for i in self.maxsulot_royhat])
#         return f'{self.dokon_nomi} nomli dokondagi maxsulotlar: \n{product}\n'
#     def mijoz_info(self):
#         odam = ''.join([n.mijoz_malumot() for n in self.mijoz_royhat])
#         return f'{self.dokon_nomi} nomli dokondagi mijozlar: \n{odam}\n'

# dokon1 = Dokon('Rustam aga')
# dokon1.add_product('Sut' , 14000)
# dokon1.add_mijoz('Ali')
# print(dokon1.maxsulot_info())
# print(dokon1.mijoz_info())

# class Spektakl:
#     def init(self , nom , muallif , davomiylik):
#         self.nom = nom
#         self.muallif = muallif
#         self.davomiylik = davomiylik
#     def malumot(self):
#         return f"'{self.nom}' , muallifi {self.muallif} , {self.davomiylik} davom qiladi"
    
# class Spektakl_qosh:
#     def init(self ):
#         self.royhat = []
#     def add_spektakl(self , nom , muallif , davomiylik):
#         spektakl = Spektakl(nom , muallif , davomiylik)
#         self.royhat.append(spektakl)
#     def info(self):
#         chiqar = '\n'.join([i.malumot() for i in self.royhat])
#         return f'Spektakllar: \n{chiqar}\n'

# teatr1 = Spektakl_qosh()
# teatr1.add_spektakl('Layli va Majnun' , 'Salim' , 1.25)
# print(teatr1.info())
# class qishloq :
#     def __init__(self ,kattaligi,nomi):
#         self.katttaligi=kattaligi
#         self.nomi=nomi
#         self.soni=0
#         self.lis=[]
#     def malumot(self):
#         return f"{self.katttaligi},{self.nomi}"
#     def add_uy (self,katttaligi,nomi):
#         ovul 
# class kitob_dokoni:
#     def __init__(self,kitob,dokoni):
#         self.kitob=kitob
#         self.dokoni=dokoni
#         self.soni=0
#         self.lis=[]
#     def malumot(self):
#         return f"{self.kitob}"
#     def add_kitob(self,kitob,dokoni):
#         book=kitob_dokoni(kitob,dokoni)
#         self.lis.append(book)
#         self.soni+=1
#     def malumot_ber(self):
#         return f"{self.dokoni} dokonida  {self.kitob} kitobi bor"
# kitob_1=kitob_dokoni("magnit","sariq devni minib")
# print(kitob_1.malumot_ber())
# class bankamat:
#     def __init__(self,hisob,pul_yechish,qoldiq):
#         self.hisob=hisob
#         self.pul=pul_yechish
#         self.qoldiq=qoldiq
#         self.lis=[]
#         self.lisa=[]
#         def malum (self,):
#             return hisob-pul_yechish
#     def malumot(self):
#         return f"sizning hisobingizda {self.hisob}min som pul bor siz {self.pul}  yechib oldinigiz va qartangizda {self.malum}"
#     def add_hisob(self,hisob,pul,qoldiq):
#         bank=bankamat(hisob,pul,qoldiq)
#         self.lis.append(bank)
# bankamat_1=bankamat(500,250)
# print(bankamat_1.malumot())
# class Bankamat:
#     def __init__(self, hisob, pul_yechish):
#         self.hisob = hisob
#         self.pul_yechish = pul_yechish
#         self.transaksiyalar = []
    
#     def qoldiq_hisoblash(self):
#         return self.hisob - self.pul_yechish
    
#     def malumot(self):
#         qoldiq = self.qoldiq_hisoblash()
#         return f"Sizning hisobingizda {self.hisob} ming som pul bor. Siz {self.pul_yechish} ming som yechib oldingiz va kartangizda {qoldiq} ming som qoldi"
    
#     def transaksiya_qoshish(self, hisob, pul_yechish):
#         yangi_transaksiya = Bankamat(hisob, pul_yechish)
#         self.transaksiyalar.append(yangi_transaksiya)

# # Test qilish
# bankamat_1 = Bankamat(500, 200)
# print(bankamat_1.malumot())
# class avto:
#     def __init__(self,madeli,yili,rangi):
#         self.madeli=madeli
#         self.yili=yili
#         self.rangi=rangi
#     def malumot(self):
#         return f"mashina madeli{self.madeli} yili {self.yili} rangi {self.rangi}"
# class mashina(avto):
#     def __init__(self, madeli, yili, rangi):
#         super().__init__(madeli, yili, rangi,probegi)
#         self.probegi=probegi
# class avto:
#     def __init__(self,madeli,turi):
#         self.madeli=madeli
#         self.turi=turi
#     def malumot (self):
#         return f"mashina madeli{self.madeli} turi {self.turi}"
# class merseders(avto):
#     def __init__(self, madeli, turi, yili):
#         super().__init__(madeli, turi,) 
#         self.yili=yili
#     def malumot_ber(self):
#         return f"mashina madeli {self.madeli} turi {self.turi}  va yili {self.yili}"
# merseders_1=merseders('maybach',"yangi",2025)
# print(merseders_1.malumot_ber())
# class ustoz:
#       def __init__(self,ismi,fani,darajasi):
#            self.fani=fani
#            self.ismi=ismi
#            self.darajasi=darajasi
#       def malumot(slef):
#          return f"ustoz ismi {self.ismi} dars beradi {self.fani} darajasi {self.darajasi} "
# class informatika_ustoz(ustoz):
#         def __init__(self, ismi, fani, darajasi):
#               super().__init__(ismi, fani, darajasi)
#         def malumot_ber (self):
#                 return f"ustoz ismi {self.ismi} dars beradi {self.fani} darajasi {self.darajasi}"
# teachers=informatika_ustoz("Mirzabek",'infarmatika',1)
# print(teachers.malumot_ber())
# class texnika:
#         def __init__(self,dokon,texnikalar):
#                 self.texnkalar=texnikalar
#                 self.dokon=dokon
#         def get_info (self):
#                 return f"{self.dokon} dokonida {self.texnkalar}"
# class zavod(texnika):
#         def __init__(self, dokon, texnikalar):
#                 super().__init__(dokon, texnikalar)
#         def malumot_ber (self):
#                 return f"{self.dokon} dokonida {self.texnkalar} mavzud"
# tex1=zavod("avto texnikalarr","kir yuvish mashinasi")
# tex2=zavod('ishonch','noutbuklar')
# print(tex1.malumot_ber())
# print(tex2.malumot_ber())
# class avto :
#         def __init__(self,turi,rang
# class shaxs:
# def __init__(sel)i,probegi):
#                 self.turi=turi
#                 self.rangi=rangi
#                 self.probegi=probegi
#         def get_info(self):
#                 return f"mashina turi {self.turi} rangi {self.rangi} probegi {self.probegi}"
# class elon (avto):
#         def __init__(self, turi, rangi, probegi):
#                 super().__init__(turi, rangi, probegi)
#         def malumot_ber(self):
#                 return f"mashina turi {self.turi} rangi {self.rangi} probegi {self.probegi}"
# mashin=elon("damas","oq","2000")
# print(mashin.malumot_ber())

# class Mahsulot:
#     def init(self , turi , narxi):
#         self.turi = turi
#         self.narxi = narxi
#     def malumot(self):
#         return f'Mahsulot turi: {self.turi}\n'
    
# class Telefon(Mahsulot):
#     def init(self, turi, narxi , brend , model , xotira):
#         super().init(turi, narxi)
#         self.brend = brend
#         self.model = model
#         self.xotira = xotira
#     def hisobla(self):
#         if self.xotira == 1:
#             return f' {self.xotira}TB'
#         elif self.xotira == 2:
#             return f' {self.xotira}TB'
#         else:
#             return f' {self.xotira}GB'
#     def get_info(self):
#         return f'{self.malumot()}{self.brend} {self.model} , xotirasi {self.hisobla()} , narxi {self.narxi}$'
    

# mahsulot1 = Telefon('Smartfon' , 860 , 'Samgung' , 'S25' , 256)
# print(mahsulot1.get_info())



                                                                                            # 9
# class Shaxs:
#     def init(self, ism , familiya , yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#         def info(self):
#             return f'{self.familiya} {self.ism} , {self.yil}yil tug\'ilgan'

# class Oqituvchi(Shaxs):
#     def init(self, ism, familiya, yil , kasb , tajriba):
#         super().init(ism, familiya, yil)
#         self.kasb = kasb
#         self.tajriba = tajriba
#     def get_info(self):
#         return f'{self.familiya} {self.ism} , {self.yil}yil tug\'ilgan , kasbi {self.kasb} va {self.tajriba}yildan buyon shu kasb egasi'
    
# shaxs1 = Oqituvchi('Ali' , 'Aliyev' , 1995 , 'Oqituvchi' , 8)
# print(shaxs1.get_info())



                                                    # 10
# class Mashina:
#     def init(self ,turi , rangi):
#         self.turi = turi
#         self.rangi = rangi
#     def malumot(self):
#         return f'{self.turi} {self.rangi} rangi'
    
# class Yuk_mashina(Mashina):
#     def init(self, turi, rangi, yuk):
#         super().init(turi, rangi)  
#         self.yuk =  yuk 
#     def info(self):
#         return f'{self.malumot()} , oziga {self.yuk} tonna yuk sigdira oladi '
    
# mashina1 =Yuk_mashina('Yuk mashina' , 'Oq' , 13)
# print(mashina1.info())


                                                            # 11
# class Uchuvchi:
#     def init(self, ism , familiya , yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#     def malumot(self):
#         return f'{self.familiya} {self.ism} {self.yil}yil tug\'ilgan'

# class Harbiy_uchuvchi(Uchuvchi):
#     def init(self, ism, familiya, yil , kasb , tajriba):
#         super().init(ism, familiya, yil)
#         self.kasb = kasb
#         self.tajriba = tajriba
#     def info(self):
#         return f'{self.malumot()} , kasbi {self.kasb} va {self.tajriba}yildan buyon {self.kasb}lik kasb egasi'
    
# shaxs1 = Harbiy_uchuvchi('Ali' , 'Aliyev' , 1993 , 'Harbiy uchuvchi' , 4)
# print(shaxs1.info())


                                                            # 12


                                                                    # 13
# class Hayvon:
#     def init(self, ovoz):
#         self.ovoz = ovoz
#     def malumot(self):
#         return f'Hayvon ovozi: {self.ovoz}'

# class Mushuk(Hayvon):
#     def init(self, ovoz, turi ):
#         super().init(ovoz)
#         self.turi = turi 
#     def info(self):
#         return f'Hayvon turi: {self.turi} , va u {self.ovoz} degan ovoz chiqaradi'
    
# class It(Hayvon):
#     def init(self, ovoz,turi ):
#         super().init(ovoz)
#         self.turi = turi
#     def info(self):
#         return f'Hayvon turi: {self.turi} , va u {self.ovoz} degan ovoz chiqaradi'
    

# hayvon1 = Mushuk('Myau' , 'Mushuk')
# hayvon2 = It('Vouv' , 'It')
# print(hayvon1.info())
# print(hayvon2.info())

# 14
# class Texnika:
#     def init(self , turi , brend , narx ):
#         self.turi = turi
#         self.brend = brend
#         self.narx = narx
#     def malumot(self):
#         return f'Texnika turi: {self.turi}\n{self.brend} '
    
# class Telefon(Texnika):
#     def init(self, turi, brend, narx , model):
#         super().init(turi, brend, narx)
#         self.model = model
#     def get_info(self):
#         return f'{self.malumot()} {self.model} , narxi {self.narx}$'

# class Kompyuter(Texnika):
#     def init(self, turi, brend, narx , model):
#         super().init(turi, brend, narx)
#         self.model = model
#     def get_info(self):
#         return f'{self.malumot()} {self.model} , narxi {self.narx}$'
    
# texnika1 = Telefon('Telefon' , 'POCO'  , 210 , 'X3pro')
# texnika2 = Kompyuter('Kompyuter' , 'Apple' ,1200 , 'MacBook Air')
# print(texnika2.get_info())
# print(texnika1.get_info())



                                            # 15
# class Kompaniya:
#     def init(self , nomi , kasbi):
#         self.nomi = nomi
#         self.kasbi = kasbi
#     def malumot(self):
#         return f'{self.nomi}'

# class Ishchi(Kompaniya):
#     def init(self, nomi, kasbi , ism , familiya):
#         super().init(nomi, kasbi)
#         self.ism = ism
#         self.familiya = familiya
#     def info(self):
#         return f'{self.malumot()} kompaniyasida {self.kasbi} bolib ishlovchi hodim {self.familiya} {self.ism}'

# ishchi1 = Ishchi('Crafers' , 'Meneger' , 'Ali' , 'Aliyev')
# print(ishchi1.info())


# class transport :
#         def __init__(self,viloyat,tuman,gazon):
#                 self.viloyat=viloyat
#                 self.tuman=tuman
#                 self.gazon=gazon
#         def malumot (self):
#                 return f"{self.viloyat} viloyati {self.tuman} tumani {self.gazon}  da"
# class bola(transport):
#         def __init__(self, viloyat, tuman, gazon,fudbolchilar,soati,fudboldoshlar):
#                 self.fudbolchilar=fudbolchilar
#                 self.fudboldoshlar=fudboldoshlar
#                 self.soati=soati
#                 super().__init__(viloyat, tuman, gazon)
#         def get_info (self):
#                 return f"{self.viloyat} viloyati {self.tuman} tumani {self.gazon}  da {self.fudbolchilar} ga qarshi {self.fudboldoshlar} oynaydi oyin {self.soati}  "
        
# bola_1=bola ("xorazm","tuprqqal'a","pitnak gazoni","Abduvaid \n Abdumajit \n Ixlosbek \n xumoyun",20:00,"Salimbek \n nizomjon \n jamshid ")
# print(bola_1.get_info())
# class transport:
#     def __init__(self, viloyat, tuman, gazon):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.gazon = gazon
    
#     def malumot(self):
#         return f"{self.viloyat} viloyati {self.tuman} tumani {self.gazon} da"

# class bola(transport):
#     def __init__(self, viloyat, tuman, gazon, fudbolchilar, soati, fudboldoshlar):
#         self.fudbolchilar = fudbolchilar
#         self.fudboldoshlar = fudboldoshlar
#         self.soati = soati
#         super().__init__(viloyat, tuman, gazon)
    
#     def get_info(self):
#         return f"{self.viloyat} viloyati {self.tuman} tumani {self.gazon} da {self.fudbolchilar} ga qarshi {self.fudboldoshlar} o'ynaydi. O'yin {self.soati} da"

# bola_1 = bola(
#     "Xorazm", 
#     "Tuproqqal'a", 
#     "Pitnak gazoni", 
#     "Abduvaid, Abdumajit, Ixlosbek, Xumoyun", 
#     "20:00", 
#     "Salimbek, Nizomjon, Jamshid"
# )

# print(bola_1.get_info())

# class Avto_dokon:
#         def init(self ,  brend , model , narx):   
#                 self.brend = brend
#                 self.model = model
#                 self.narx=  narx
#         def malumot(self):
#                 return f'{self.brend} {self.model}'
        
# class Mashina(Avto_dokon):
#         def init(self, brend, model, narx , rang  , probeg):
#                 super().init(brend, model, narx)
#                 self.rang =rang
#                 self.probeg = probeg
#         def info(self):
#                 return f'{self.brend} {self.model} narxi {self.narx}$ , {self.rang} rangli , {self.probeg}km yurgan'
# avto1 = Mashina('Mersedes' , 'E63' , '13600' , 'oq' , '142000')
# avto2 = Mashina('KIA' , 'K5' , '35000' , 'oq' , '2000')
# print(avto1.info())
# print(avto2.info())

# yolvchi
                                                                                                # 17
# class Transport:
#         def init(self, nomi , turi , sonli):
#                 self.nomi = nomi
#                 self.turi = turi
#                 self.sonli = sonli
#         def malumot(self):
#                 return f'{self.turi}\n{self.nomi} kompamiyasiga tegishli , {self.sonli} sonli {self.turi}.'
# class Poyezd(Transport):
#         def init(self, nomi, turi , sonli , uchun , vagon):
#                 super().init(nomi, turi , sonli)
#                 self.uchun = uchun
#                 self.vagon = vagon
#         def yonalish(self , qayerdan , qayerga ):
#                 self.qayerdan = qayerdan
#                 self.qayerga = qayerga
#         def bilet(self , narxi):
#                 self.narxi = narxi
#         def get_poezd(self):
#                 return f'{self.malumot()}. Bu poyezd {self.uchun} uchun , {self.vagon}ta vagondan iborat va bu poyezdning yonalishi {self.qayerdan}-{self.qayerga}. Chipta narxi {self.bilet}so\'m.'
        
# class Avtobus(Transport):
#         def init(self, nomi, turi, sonli , sigim ,yili):
#                 super().init(nomi, turi, sonli)
#                 self.sigim = sigim
#                 self.yili = yili
#         def chipta(self , narx):
#                 self.narx = narx
#         def yonalish(self , qayerdan , qayerga ):
#                 self.qayerdan = qayerdan
#                 self.qayerga = qayerga
#         def get_avtobus(self):
#                 return f'{self.malumot()}. Bu avtobus {self.yili}yil ushlab chiqaarlingan bolib oziga {self.sigim} nafar odam sigdira oladi va bu avtobusning yonalishi {self.qayerdan}-{self.qayerga}. Chipta narxi {self.chipta}so\'m.' 

# transport1 = Poyezd('O\'zTY' , 'Poyezd' , 'W418' , 'yolivchi tashish' , 37)
# transport1.yonalish('Toshkent' , 'Xorazm')
# transport1.bilet(362000)
# print(transport1.get_poezd())



                                                                        # 18
# class Shaxs:
#         def init(self , ism , familiya , yil):
#                 self.ism = ism
#                 self.familiya = familiya
#                 self.yil = yil
#         def malumot(self):
#                 return f'{self.familiya} {self.ism} , {self.yil}yil tugilgan.'
        
# class Talaba(Shaxs):
#         def init(self, ism, familiya, yil , univer , kurs):
#                 super().init(ism, familiya, yil)
#                 self.univer = univer
#                 self.kurs = kurs
#         def fakultet(self , nomi):
#                 self.nomi = nomi
#         def yangilash(self):
#                 self.kursi +=1
#         def end_univer(self):
#                 if self.kursi == 4:
#                         return 'Bitiruvchi talaba'
#         def get_student(self):
#                 return f'{self.malumot()} {self.univer} universitetida {self.nomi} fakultetidan talim oladi , {self.kurs}-kurs'
# class Oqituvchi(Shaxs):
#         def init(self, ism, familiya, yil , maktab ):
#                 super().init(ism, familiya, yil)
#                 self.maktab = maktab
#         def fan(self, fan_nomi):
#                 self.fan_nomi = fan_nomi
#         def tajriba(self , opit):
#                 self.opit = opit
#         def yangilash(self):
#                 self.opit +=1
#         def get_teacher(self):
#                 return f'{self.malumot()} {self.maktab} maktabida {self.fan_nomi} fanidan talim beradi , {self.opit}yil tajribaga ega'

# shaxs1 = Oqituvchi('ALi' , 'Aliyev' , '1996' , '2-Sizov')
# shaxs1.fan('Makematika')
# shaxs1.tajriba(7)
# shaxs1.yangilash()
# print(shaxs1.get_teacher())


                                                                                        # 19
# class Maxsulot:
#         def init(self , nomi , narxi):
#                         self.nomi = nomi
#                         self.narxi = narxi
#                 def malumot(self):
#                         return f'{self.nomi} , narxi {self.narxi}so\'m'
                
#         class Meva(Maxsulot):
#                 def init(self, nomi, narxi , turi):
#                         super().init(nomi, narxi)
#                         self.turi = turi
#                 def muddat(self , muddat):
#                         self.muddat = muddat
#                 def davlat(self , qayer):
#                         self.qayer = qayer
#                 def get_meva(self):
#                         return f'Maxsulot: {self.nomi}\n{self.turi} , narxi{self.narxi}so\'m. Dokonga {self.muddat}yil {self.qayer} shahridan kelgan.'

#         maxsulot1 = Meva('Meva' , 30000 , 'Marakuya')
#         maxsulot1.muddat('10.27.2025') 
#         maxsulot1.davlat('Avstraliya')
#         print(maxsulot1.get_meva())


# class Bino:
#         def init(self  , manzil , narx):
#                 self.manzil = manzil
#                 self.narx = narx
#         def malumot(self):
#                 return f'{self.manzil} , narxi {self.narx}$'
        
# class Uy(Bino):
#         def init(self, manzil, kv , narx ,   honalar):
#                 super().init(manzil, narx)
#                 self.honalar = honalar
#                 self.kv=  kv
#         def remont(self , remont):
#                 self.remont = remont
#         def xaq(self , turi, uzunlik , balandlik ,  kenglik , kv_narx):
#                 self.turi = turi
#                 self.uzunlik = uzunlik
#                 self.balandlik = balandlik
#                 self.kenglik =  kenglik
#                 self.kv_narx = kv_narx
#         def get_xaq(self):
#                 return f'Xizmat turi: {self.turi}\nXona uzunliki {self.uzunlik}m\nXona kengliki {self.kenglik}m\nXona balantliki: {self.balandlik}m\n1kv narx : {self.kv_narx}$\nJami usta xaqqi: {(self.uzunlik * self.kenglik * self.balandlik) * self.kv_narx}$'
#         def xonalar_maydoni(self , xonalar_maydoni):
#                 self.xonalar_maydoni = xonalar_maydoni
#         def get_info(self):
#                 return f'Manzil: {self.manzil} {self.kv}kv\nNarxi: {self.narx}$\nHonalar soni: {self.honalar}ta\nRemont: {self.remont}.\nXonalar maydoni {self.xonalar_maydoni}m²'
        
# uy1 = Uy('3/8A' , '24' , 30000 , 4)
# uy1.remont('Evro')
# uy1.xaq('Pol taxta' , 8 , 1 , 5 , 2)
# uy1.xonalar_maydoni(20)
# print(uy1.get_xaq())
        

                                                                                # 21
# class Avto:
#         def init(self, model, yil, tezlik):
#                 self.model = model
#                 self.yil = yil
#                 self.tezlik = tezlik

#         def info(self):
#                 return f"Model: {self.model}\nYil: {self.yil}yil\nTezlik: {self.tezlik}km/h"


# class SportAvto(Avto):
#         def init(self, model, yil, tezlik, turi):
#                 super().init(model, yil, tezlik)
#                 self.turi = turi

#         def get_info(self):
#                 return f'{self.info()}\nMashina turi: {self.turi}'


# sport = SportAvto("BMW M5", 2023, 330, 'Turbo')
# print(sport.get_info())

                                                                                # 22
# class Kitob:
#         def init(self, nomi, muallif, sahifa):
#                 self.nomi = nomi
#                 self.muallif = muallif
#                 self.sahifa = sahifa

#         def malumot(self):
#                 return f"Nomi: {self.nomi}\nMuallif: {self.muallif}\nSahifa: {self.sahifa}bet"


# class ElektronKitob(Kitob):
#         def init(self, nomi, muallif, sahifa_soni, fayl_hajmi, formati):
#                 super().init(nomi, muallif, sahifa_soni) 
#                 self.fayl_hajmi = fayl_hajmi
#                 self.formati = formati

#         def info(self):
#                return f'{self.malumot()}\nFayl hajmi: {self.fayl_hajmi}MB\nKitob formati: {self.formati}'
        

# kitob = ElektronKitob('Layli va Majnun' , 'Alisher Navoi', 450, 8, "Elektron")
# print(kitob.info())


                                                                                        # 23
# class Avto:
#     def init(self , brend ,  model , yil ):
#         self.brend  = brend
#         self.model = model
#         self.yil = yil

#     def malumot(self):
#         return f"{self.brend} {self.model}, {self.yil}yil ishlab chiqarlingan"

# class Elektro_Avto(Avto):
#     def init(self, brend, model, yil , batareya):
#         super().init(brend, model, yil)
#         self.batareya = batareya

#     def zaryad_qoshish(self, foiz):
#         self.foiz = foiz
#         return f"Mashinang zaryadlangandan keyingi zaryadi:{self.batareya + self.foiz}%"

#     def zaryad_foiz(self):
#         return f"Hozirgi batareya darajasi: {self.batareya}%"

#     def get_info(self):
#         return f'{self.brend} {self.model}, {self.yil}yil ishlab chiqarlingan , mashinaning zaryadi: {self.batareya}%'


# avto1 = Elektro_Avto('BYD' , 'Chempion' , 2024  , 45)
# print(avto1.get_info())
# print(avto1.zaryad_qoshish(30))


                        # 24
# class Son:
#     def init(self , a , b):
#         self.a = a
#         self.b = b

# class Hisobla(Son):
#     def init(self, a, b):
#         super().init(a, b)

#     def qosh(self):
#         return f'{self.a} ga {self.b} ni qoshsa {self.a + self.b} boladi'
    
#     def ayir(self):
#         return f'{self.a} dan {self.b} ni ayirsa {self.a - self.b} boladi'
    
#     def kopaytir(self):
#         return f'{self.a} ga {self.b} ga kopaytirsa {self.a * self.b} boladi'
    
#     def bol(self):
#         return f'{self.a} ni {self.b} ga bolsa {self.a / self.b} boladi'
    
# son1 = Hisobla(5,4)
# print(son1.kopaytir())

# class hayvon:
#         def __init__(self,hayvon):
#                 self.hayvon=hayvon
#         def malumot (self):
#                 return f"{self.hayvon}"
# class qush(hayvon):
#         def __init__(self, hayvon,uchish,ovozi,tezligi):
#               super().__init__(hayvon,)
#               self.uchish=uchish
#               self.ovozi=ovozi
#               self.tezligi=tezligi
#         def get_info(self):
#                 return f"{self.hayvon} hayvonining ovozi {self.ovozi}  u {self.uchish} balandlikdagi tezligi {self.tezligi} dan oshadi"
# class                  

# class Hayvon:
#     def __init__(self, nomi, yoshi):
#         self.nomi = nomi
#         self.yoshi = yoshi
    
#     def ovqatlanish(self):
#         print(f"{self.nomi} ovqatlanmoqda.")
    
#     def uxlab_yotish(self):
#         print(f"{self.nomi} uxlab yotibdi.")

# class Qush(Hayvon):
#     def __init__(self, nomi, yoshi, qanot_uzunligi, tezligi, ovozi):
#         super().__init__(nomi, yoshi)      
#         self.qanot_uzunligi = qanot_uzunligi  
#         self.tezligi = tezligi              
#         self.ovozi = ovozi                  
#         self.uchishi = True                  
    
#     def nomi(self):
#         return self.nomi
    
#     def uchishi_mumkinmi(self):
#         if self.uchishi:
#             print(f"{self.nomi} uchishi mumkin!")
#         else:
#             print(f"{self.nomi} uchmaydi (masalan, pingvin yoki tuyaqush).")
#         return self.uchishi
    
#     def uchish_tezligi(self):
#         print(f"{self.nomi}ning uchish tezligi: {self.tezligi} km/soat")
#         return self.tezligi
    
#     def ovoz_chiqar(self):
#         print(f"{self.nomi}: {self.ovozi}")
    
#     def qanot_uzunligini_korsat(self):
#         print(f"{self.nomi}ning qanot uzunligi: {self.qanot_uzunligi} metr")
#         return self.qanot_uzunligi
    
#     def yoshini_ayt(self):
#         print(f"{self.nomi}ning yoshi: {self.yoshi} yosh")
#         return self.yoshi
    
#     def malumotlarni_chiqar(self):
#         print("\n" + "="*40)
#         print(f"Qush: {self.nomi}")
#         print(f"Yoshi: {self.yoshi}")
#         print(f"Qanot uzunligi: {self.qanot_uzunligi} m")
#         print(f"Uchish tezligi: {self.tezligi} km/soat")
#         print(f"Ovozi: {self.ovozi}")
#         print(f"Uchishi mumkinmi: {'Ha' if self.uchishi else 'Yo‘q'}")
#         print("="*40 + "\n")

# burgut = Qush(
#     nomi="Oltin burgut", 
#     yoshi=8, 
#     qanot_uzunligi=2.3, 
#     tezligi=320, 
#     ovozi="Qiyqiriq ovozi: Kiii-aaa!"
# )

# laylak = Qush("Oq laylak", 4, 1.9, 70, "Klap-klap (tumshug‘i bilan)")
# pingvin = Qush("Imperotor pingvin", 6, 1.1, 0, "Karr-karr", )
# pingvin.uchishi = False   

# burgut.malumotlarni_chiqar()
# burgut.uchishi_mumkinmi()
# burgut.uchish_tezligi()
# burgut.ovoz_chiqar()

# laylak.malumotlarni_chiqar()
# pingvin.malumotlarni_chiqar()
# pingvin.uchishi_mumkinmi()  
# class student:
#     def __init__(self,talaba_ismi,talab_yoshi,):
#         self.ismi=talaba_ismi
#         self.yoshi=talab_yoshi
#     def malumot(self):
#         return f"{self.ismi}, {self.yoshi}"
# class talaba (student):
#     def __init__(self, talaba_ismi, talab_yoshi,unverstiteti):
#         super().__init__(talaba_ismi, talab_yoshi)
#         self.unverstitendi=unverstiteti
#     def get_info (self)
#        return f""
import re


class avtomabillar:
    def __init__(self,kampanya,mashina_turi,narxi):
        self.kampaniya=kampanya
        self.turi=mashina_turi
        self.narxi=narxi
    def malumot_1(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} va uning narxi {self.narxi} milion"
class meros(avtomabillar):
    def __init__(self, kampanya, mashina_turi, narxi,extiyot_qisimlari,narxlari,dokonlari,malumoti,malumotari,summasi):
        super().__init__(kampanya, mashina_turi, narxi)
        self.qisimlari=extiyot_qisimlari
        self.narxlari=narxlari
        self.dokon=dokonlari
        self.malumoti=malumoti
        self.malumotlari=malumotari
        self.summasi=summasi
    def jentra(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
   
    def cobalt(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
   
    def malibu2(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
    
    def onix (self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
   
    def taheo(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
    
    def Kompakt_sedan(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"

    def Offroad_SUV(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"

    def Coupe_sedan(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
    
    def Elektr_sedan (self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"

    def gelik(self):
        return f"{self.kampaniya} kampanyasining yangi chiqayotgan avtomabili {self.turi} madelining narxi {self.narxi} milion vaextiyot qisimlari  {self.qisimlari} bularning narxlari{self.narxlari} bu extiyot qisimlari {self.dokon} dokonlarida bor"
    
chevralet1=meros("chevralet","jentra",160 000 00 ,"aptechka zaxira balon",400 000,"uz avto,avtosalon")
print(chevralet1.jentra())
print(chevralet1.cobalt())
print(chevralet1.malibu2())
print(chevralet1.onix())
print(chevralet1.taheo())
print(chevralet1.Kompakt_sedan())
print(chevralet1.Offroad_SUV())
print(chevralet1.Coupe_sedan())
print(chevralet1.Elektr_sedan())
print(chevralet1.gelik())



