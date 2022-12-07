def garis1():
    print ("================================")

def garis2():
    print ("--------------------------------")
    
# Table buku 😓
bukuTable = []

# me when disuruh pake class 👀

class isi:
    def delete(self):
        indeks = int(input("Inputkan ID Buku : "))
        if indeks > len(bukuTable):
            print("ID SALAH")
        else:
            bukuTable.remove(bukuTable[indeks])
        garis1()
        print ("Buku berhasil dihapus!")
        garis2()
    
    def masukan(self):
        garis1()
        buku_baru = input("Judul Buku : ")
        bukuTable.append(buku_baru)
        print("Buku Berhasil ditambah!")
        garis1()
    
    def lihat(self):
        if len(bukuTable) <= 0:
            garis1()
            print("Lah kosong?")
        else:
            for indeks in range(len(bukuTable)):
                garis1()
                print("[{}] {}".format(indeks, bukuTable[indeks]))
                garis1()
    
    def edit(self):
        indeks = int(input("Masukkan ID buku : "))
        if indeks > len(bukuTable):
            print("ID Buku Salah")
            garis2()
        else:
            judul_baru = input("Masukkan Judul Buku Baru : ")
            bukuTable[indeks] = judul_baru
            garis2()
            print ("Buku Berhasil Di Ubah")
            garis1()


def ambatukam():
    #class ges ya
    class buku:
        def __init__(self,masukan,delete,edit,lihat):
            self.masukan = masukan
            self.delete = delete
            self.edit = edit
            self.lihat = lihat;

    buku = buku(1,2,3,4)

    print('------ini adalah Perpustakaan Online Heil Aurora-------')
    print(f'masukan = {buku.masukan}')
    print(f'delete = {buku.delete}')
    print(f'edit = {buku.edit}')
    print(f'perlihatkan = {buku.lihat}')

    input1 = int(input("Masukan Pilihan : "))

    obj = isi()

    #me when percabangan 😱

    if input1 == 1:
        obj.masukan()
    elif input1 == 2:
        obj.delete()
    elif input1 == 3:
        obj.edit()
    elif input1 == 4:
        obj.lihat()

# tampilkan Menu 😁
if __name__ == "__main__":
    while True:
        ambatukam()