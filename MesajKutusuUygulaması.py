def menu():
    """Menüyü ekrana yazdırır."""
    print("1. Mesaj Gönder")
    print("2. Mesajları Göster")
    print("3. Çıkış")

def mesaj_gonder(mesajlar):
    """Mesaj gönderme işlemini gerçekleştirir."""
    gonderen = input("Gönderen: ")
    alici = input("Alıcı: ")
    mesaj = input("Mesaj: ")
    
    # Boş değerlerin girilmesini engellemek için kontrol
    if gonderen and alici and mesaj:
        mesajlar.append({"gonderen": gonderen, "alici": alici, "mesaj": mesaj})
        print("Mesaj gönderildi!")
    else:
        print("Gönderen, alıcı ve mesaj boş olamaz.")

def mesajlari_goster(mesajlar):
    """Mesajları listeler."""
    if not mesajlar:
        print("Hiç mesaj yok.")
    else:
        for i, mesaj in enumerate(mesajlar):
            try:
                print(f"{i + 1}. {mesaj['gonderen']} -> {mesaj['alici']}: {mesaj['mesaj']}")
            except KeyError as e:
                print(f"Mesajda eksik bilgi var: {e}")

def main():
    """Ana program döngüsünü başlatır."""
    mesajlar = []
    while True:
        menu()
        secim = input("Bir seçenek girin: ")
        if secim == "1":
            mesaj_gonder(mesajlar)
        elif secim == "2":
            mesajlari_goster(mesajlar)
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
