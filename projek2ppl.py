#fungsi garisnya kids 
def garis1():
    print ("            ")

def garis2():
    print ("--------------------------------")

# Perpus kosong untuk menyimpan buku
buku = []

# fungsi show buku ( perlihatkan buku )
def perlihatkan_buku():
    if len(buku) <= 0:
        garis1()
        print ("Buku Kosong, Tolong Masukkan Judul!")
        garis1()
    else: 
        for indeks in range(len(buku)):
            print ("[{}]] {}".format (indeks, buku [indeks]))
        
# fungsi untuk edit buku
def edit_buku():
    perlihatkan_buku()
    indeks = int(input("Inputkn ID buku : "))
    if indeks > len(buku):
        print("ID SALAH")
        garis2()
    else: 
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("Buku berhasil dirubah!")
        perlihatkan_buku()
        garis1()
        
# fungsi insert buku
def tambah_buku():
    garis1()
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print ("Buku Berhasil ditambah!")
    garis1()

#fungsi delete buku
def delete_buku():
    perlihatkan_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print ("ID SALAH")
    else:
        buku.remove(buku[indeks])
        garis1()
        print ("Buku Berhasil dihapus!")
        garis2()




# Menu untuk tampilan perpus
def perlihatkan_menu():
    print ("\n")
    print ("----Selamat Datang Di Perpustakaan Heil Aurora----")
    print ("1. Perlihatkan buku")
    print ("2. Tambah buku")
    print ("3. Edit buku")
    print ("4. Delete buku")
    print ("5. Keluar")
    
    menu = int(input("Pilih Menu : > "))
    
    if menu == 1:
        perlihatkan_buku()
    elif menu == 2:
        tambah_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Maaf Salah, Ulang Kembali!")
    
# tampilkan Menu
if __name__ == "__main__":
    while True:
        perlihatkan_menu()
    
