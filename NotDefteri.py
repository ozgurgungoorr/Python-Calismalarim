def menu():
    print("1. Not Ekle")
    print("2. Notları Göster")
    print("3. Çıkış")

def not_ekle(notlar):
    not_metni = input("Not Metni: ")
    if not_metni:
        notlar.append(not_metni)
        print("Not eklendi!")
    else:
        print("Not metni boş olamaz.")

def notlari_goster(notlar):
    if not notlar:
        print("Hiç not yok.")
    else:
        for i, not_metni in enumerate(notlar):
            print(f"{i + 1}. {not_metni}")

def main():
    notlar = []
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "1":
            not_ekle(notlar)
        elif secim == "2":
            notlari_goster(notlar)
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
