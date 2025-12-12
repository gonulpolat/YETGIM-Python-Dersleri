"""
    **Yaş Gün Hesaplayıcı**: Doğum tarihinden bugüne kaç gün yaşandığını hesaplayan program
"""

import datetime

bugun = datetime.date.today()
dogum_tarihi_input = input("Doğum tarihinizi girin (GG.AA.YYYY): ")
gun, ay, yil = map(int, dogum_tarihi_input.split('.'))
dogum_tarihi = datetime.date(yil, ay, gun)
fark = bugun - dogum_tarihi

print(f"Doğduğunuz günden beri {fark.days} gün geçti.")
