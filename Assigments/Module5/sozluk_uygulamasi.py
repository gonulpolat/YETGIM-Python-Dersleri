"""
    **Sözlük Uygulaması**: Türkçe-İngilizce kelime çevirme programı

    Tkinter ile yazılabilir
"""

sozluk = {
    "Kitap" : "Book",
    "Masa" : "Table",
    "Bilgisayar" : "Computer",
    "Kalem" : "Pencil",
    "Televizyon": "Television",
    "Uzaktan Kumanda" : "Remote",
}

def translate():
    print("Türkçe - İngilizce Sözlük")
    girdi = input("----------> ")
    for key, value in sozluk.items():
        if key == girdi.title():
            print(value)
            break
        elif value == girdi.title():
            print(key)
            break
    else:
        print("Maalesef bu zorlu kelimeye erişm sağlanamıyor!")

translate()
