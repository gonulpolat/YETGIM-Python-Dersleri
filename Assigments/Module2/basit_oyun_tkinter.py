"""
    Tkinter kütüphanesi ile Taş-Kağıt-Makas oyunu

    YAZILABİLİR 
"""

import tkinter as tk
import random
from basit_oyun import play

score_oyuncu     = 0
score_bilgisayar = 0


root = tk.Tk()    # ana windowu oluştur
root.title("Taş - Kağıt - Makas")    # windowun başlığı
root.geometry("500x400")

result_label = tk.Label(root, text="Seçiminizi yapın", font=("Arial", 14))
result_label.pack(pady=20)



btn_frame = tk.Frame(root)  # Butonlar için frame
btn_frame.pack(pady=10)

btn_tas = tk.Button(btn_frame, text="Taş", width=10, command=lambda: play("Taş"))
btn_tas.grid(row=0, column=0, padx=5)

btn_kagit = tk.Button(btn_frame, text="Kağıt", width=10, command=lambda: play("Kağıt"))
btn_kagit.grid(row=0, column=1, padx=5)

btn_makas = tk.Button(btn_frame, text="Makas", width=10, command=lambda: play("Makas"))
btn_makas.grid(row=0, column=2, padx=5)


score_frame = tk.Frame(root)     # Skorlar için frame
score_frame.pack(pady=10)

user_label = tk.Label(score_frame, text="Kullanıcı: 0", font=("Arial", 12))     # Kullanıcı skoru
user_label.grid(row=0, column=0, padx=20)

comp_label = tk.Label(score_frame, text="Bilgisayar: 0", font=("Arial", 12))    # Bilgisayar skoru
comp_label.grid(row=0, column=1, padx=20)

# Tur geçmişi için frame
history_frame = tk.Frame(root)
history_frame.pack(pady=10, fill=tk.BOTH, expand=True)

history_text = tk.Text(history_frame, height=10, width=40, font=("Arial", 12))
history_text.pack()


score_oyuncu, score_bilgisayar = play()








root.mainloop()



