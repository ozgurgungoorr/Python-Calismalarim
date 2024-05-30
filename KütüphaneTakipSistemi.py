def menu():
    print("1. Kitap Ekle")
    print("2. Kitapları Göster")
    print("3. Çıkış")
    
    
def Kitap_ekle(kitaplar):
    isim = input("Kitap ismi: ")
    yazar = input("Yazar: ")
    if isim and yazar:
        kitaplar.append({"isim": isim, "yazar": yazar})
        print("Kitap eklendi!")
    else:
        print("Kitap ismi ve yazar boş bırakılamaz.")

def Kitapları_goster(kitaplar):
    if not kitaplar:
        print("Hiç kitap yok.")
    else:
        for i, kitap in enumerate(kitaplar):
            print(f"{i + 1}. {kitap['isim']} - {kitap['yazar']}")
            
def main():
    kitaplar = []
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "1":
            Kitap_ekle(kitaplar)
        elif secim == "2":
            Kitapları_goster(kitaplar)
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek lütfen tekrar deneyin.")       
            
if __name__=="__main__":
    main()