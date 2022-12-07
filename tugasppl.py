class manusia():
    def _init_(self, nama, agama ):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print(self.nama,"beragama",self.agama)

class sholat(manusia):
    def _init_(self, nama, agama, caraberibadah):
        manusia._init_(self,nama, agama)
        self.caraberibadah = caraberibadah

class sembahyang(manusia):
    def _init_(self, nama, agama, carasembahyang):
        manusia._init_(self,nama, agama)
        self.carasembahyang = carasembahyang


#menampilkan
hisyam = sholat('hisyam','islam','sholat')
hisyam.perkenalan()
print(f'hisyam beribadah dengan melakukan {hisyam.caraberibadah}\n')

abraham = sembahyang('abraham','kristen','sembahyang')
abraham.perkenalan()
print(f'abraham beribadah dengan melakukan {abraham.carasembahyang}')