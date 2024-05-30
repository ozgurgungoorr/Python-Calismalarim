def menu():
    print("1. Adım Ekle")
    print("2. Adımları göster")
    print("3. Çıkış")
    
def adim_ekle(adimlar):
    adim = int(input("Eklenecek adım sayisini girin: "))
    if adim > 0:
       adimlar.append(adim)
       print("Adim eklendi!")
    else:
        print("Adım sayisi pozitif olmalı.")
        
def adimlari_goster(adimlar):
    if not adimlar:
        print("Hiç adim yok.")
    else:
        toplam_adim = sum(adimlar)
        print(f"Toplam adım: {toplam_adim}")
        
def main():
    adimlar = []
    while True:
        menu()
        secim = input("Bir seçeenk girin: ")
        if secim == "1":
            adim_ekle(adimlar)
        elif secim == "2":
            adimlari_goster(adimlar)
        elif secim == "3":
            print("Çıkış yapiliyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyiniz.")
            
            
if __name__ == "__main__":
    main()