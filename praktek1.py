class siswa : 
    def __init__(self, nama) :
        self.nama = nama

#institiansi 
jp_1 = siswa('euroski')

#print 
print(f'1. Siswa kami bernama {jp_1.nama} Ganteng\n')

class guru :
    def __init__(self,nama):
        self._nama = nama
    
class guru_otkp(guru): #class turunan
    def __init__(self, nama):
        super().__init__(nama) #panggil merk dibagian sini
        self._nama = nama
        
    def nama(self):
        # hak akses_merk dari subclass
        print (f'2. Guru kami bernama {self._nama} Yang Cantik\n') 

#instansiasi
mengajar = guru_otkp('Bu Anita')
mengajar.nama()

class kepsek :
    def __init__(self, nama):
        self.__nama = nama
        
    def tampilkan_nama(self):
        print(f'3. Kepsek kami bernama {self.__nama}\n')

kepse = kepsek('Pak lilik')
kepse.tampilkan_nama()