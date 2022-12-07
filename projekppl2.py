baju = []

def show_data():
    if len(baju) <= 0:
        print ("belum ada stok")
    else: 
        for indeks in (len(baju)):
            print ("[%d]" %s % (indeks, buku[indeks]))
            
def insert_data():
    baju = input('merk baju: ')
    baju.append (baju)
    
def edit_data():
    show_data()
    indeks = input('inputkan merk baju: ')
    if(indeks > len(baju)):
        print ("merk salah")
    else:
        baju = input("baju baru: ")
        baju[indeks] = baju_baru    

def delete_data():
    show_data()
    indeks = input("masukan merk baju: ")
    if(indeks > len(baju)):
        print ("merk salah")
    else: 
        baju.remove(baju[indeks])

def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] show_data")
    print ("[2] insert_data")
    print ("[3] edit_data")
    print ("[4] delete_data")
    print ("[5] exit")
    menu = input("PILIH MENU: ")
    print ("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print ("Salah pilih!")


if __name__ == "__main__":

    while():
        show_menu()