#Membuat Operator Overloading
class Angka:
    def __init__(self, angka):
        self.angka = angka
    
    def __add__(self, objek):
        return self.angka + objek.angka
    
# Ketika kita panggil 
x1 = (10)
x2 = (20)

# kita bisa mereturn instan baru dari kelas Angka agar hasilnya tetap konsisten. 
class Angka:
    def __init__(self, angka):
        self.angka = angka
    
    def __add__(self, objek):
        return angka(
            self.angka + objek.angka
        )
#Ketika dipanggil 
x1 = (5)
x2 = (20)
x3 = x1 + x2

#Print Hasil
print (x3.angka)

#menangani operator perbandingan
class Angka:
    def __init__(self, angka):
        self.angka = angka
    
    def __gt__(self, objek):
        return self.angka > objek.angka

    def __it__(self, objek):
        return self.angka < objek.angka
    
    def __eq__(self, objek):
        return self.angka == objek.angka
    
#Membandingkan antar dua objek dari kelas Angka
x1 = (20)
x2 = (10)

print(x1 > x2)
print(x1 < x2)
print(x1 == x2)

#output : True, False , False