"""
    **Sınıf Geçme Sistemi**: Kullanıcıdan notları alıp sınıf geçip geçmediğini, harf notunu gösteren program
"""

def pass_lecture(m1, m2, f):
    avg = calculate_average(m1, m2, f)
    if avg > 100 or avg < 0:
        print("Notlarınızı yanlış girdiniz!")
    else:
        if avg >= 90:
            harf = "AA"
        elif avg >= 85:
            harf = "BA"
        elif avg >= 80:
            harf = "BB"
        elif avg >= 70:
            harf = "CB"
        elif avg >= 60:
            harf = "CC"
        elif avg >= 55:
            harf = "DC"
        elif avg >= 50:
            harf = "DD"
        else:
            harf = "FF"

        print(f"Harf notunuz   : {harf}")
        print(f"Not ortalamanız: {avg}")
    

def calculate_average(m1, m2, f):
    return (m1 + m2) * 0.2 + f * 0.6


if __name__ == "__main__":
    while True:
        try:
            midterm1 = float(input("İlk vize   : "))
            midterm2 = float(input("İkinci vize: "))
            final = float(input("Final      : "))
            break
        except:
            print("Lütfen notlarınızı sayısal değer giriniz.")
    pass_lecture(midterm1, midterm2, final)
