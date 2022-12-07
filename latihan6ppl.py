# Jenis enkapsulasi : public, protected, private

# Membuat public class

class segitiga :
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;
        
#institiansi 
segitiga_besar = segitiga(100, 80)

#print 
print('Ini adalah public class')
print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

#Membuat protected class

class mobil: #class induk
    def __init__(self, merk):
        self._merk = merk #protected class declaration
        
class mobilefwan(mobil): #class turunan
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk dibagian sini
        self._total_gear = total_gear
        
    def pamer(self):
        # hak akses_merk dari subclass
        print (f'ini adalah mobil {self._merk} dengan totalgear {self._total_gear}\n') 

#instansiasi
print('ini adalah protected class')
ferrari = mobilefwan('Ferrari ',8)
ferrari.pamer()

#membuat private class 
class motor:
    def __init__(self, merk):
        self. __merk = merk #private class declaration
        
    def tampilkan_merk (self):
        print(f'Merk motornya : {self.__merk}')
        #panggil private disini
        
#instansiasi
print('Ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()
        
        
