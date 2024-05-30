def kelime_sayaci(metin):
    kelimeler = metin.split()
    return len(kelimeler)

if __name__=="__main__":
    metin = input("Metni girin: ")
    sayi = kelime_sayaci(metin)
    print(f"Metindeki kelime sayisi: {sayi}")
