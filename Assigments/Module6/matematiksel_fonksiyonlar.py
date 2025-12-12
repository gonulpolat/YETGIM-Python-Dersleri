"""
    **Matematiksel Fonksiyonlar**: Trigonometri, logaritma, istatistik fonksiyonları
"""

import tkinter as tk
from tkinter import ttk, messagebox

from trigonometri import sin_derece, cos_derece, tan_derece, arcsin_derece, arccos_derece, arctan_derece
from logaritma import dogal_log, log10, log2, log_b
from istatistik import ortalama, medyan, mod, standart_sapma


class Matematik:
    def __init__(self, root):
        self.root = root
        self.root.title("Matematiksel Fonksiyonlar")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.trig_frame = ttk.Frame(self.notebook)
        self.log_frame = ttk.Frame(self.notebook)
        self.istatistik_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.trig_frame, text="Trigonometri")
        self.notebook.add(self.log_frame, text="Logaritma")
        self.notebook.add(self.istatistik_frame, text="İstatistik")

        self._setup_trigonometri_tab()
        self._setup_logaritma_tab()
        self._setup_istatistik_tab()


    def _setup_trigonometri_tab(self):
        ttk.Label(self.trig_frame, text="Açı (derece):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.trig_entry = ttk.Entry(self.trig_frame, width=20)
        self.trig_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(self.trig_frame, text="sin", command=lambda: self._hesapla(self._sin_hesapla)).grid(row=1, column=0, padx=10, pady=5)
        ttk.Button(self.trig_frame, text="cos", command=lambda: self._hesapla(self._cos_hesapla)).grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.trig_frame, text="tan", command=lambda: self._hesapla(self._tan_hesapla)).grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self.trig_frame, text="Değer [-1,1]:").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.trig_ters_entry = ttk.Entry(self.trig_frame, width=20)
        self.trig_ters_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(self.trig_frame, text="arcsin", command=lambda: self._hesapla(self._arcsin_hesapla)).grid(row=3, column=0, padx=10, pady=5)
        ttk.Button(self.trig_frame, text="arccos", command=lambda: self._hesapla(self._arccos_hesapla)).grid(row=3, column=1, padx=10, pady=5)
        ttk.Button(self.trig_frame, text="arctan", command=lambda: self._hesapla(self._arctan_hesapla)).grid(row=3, column=2, padx=10, pady=5)

        self.trig_sonuc = ttk.Label(self.trig_frame, text="Sonuç: ", font=("Arial", 10, "bold"))
        self.trig_sonuc.grid(row=4, column=0, columnspan=3, pady=15)

    def _sin_hesapla(self):
        derece = float(self.trig_entry.get())
        return f"sin({derece}°) = {sin_derece(derece):.6f}"

    def _cos_hesapla(self):
        derece = float(self.trig_entry.get())
        return f"cos({derece}°) = {cos_derece(derece):.6f}"

    def _tan_hesapla(self):
        derece = float(self.trig_entry.get())
        return f"tan({derece}°) = {tan_derece(derece):.6f}"

    def _arcsin_hesapla(self):
        deger = float(self.trig_ters_entry.get())
        return f"arcsin({deger}) = {arcsin_derece(deger):.2f}°"

    def _arccos_hesapla(self):
        deger = float(self.trig_ters_entry.get())
        return f"arccos({deger}) = {arccos_derece(deger):.2f}°"

    def _arctan_hesapla(self):
        deger = float(self.trig_ters_entry.get())
        return f"arctan({deger}) = {arctan_derece(deger):.2f}°"


    def _setup_logaritma_tab(self):
        ttk.Label(self.log_frame, text="x (pozitif):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.log_x_entry = ttk.Entry(self.log_frame, width=20)
        self.log_x_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(self.log_frame, text="ln(x)", command=lambda: self._hesapla(self._ln_hesapla)).grid(row=1, column=0, padx=10, pady=5)
        ttk.Button(self.log_frame, text="log₁₀(x)", command=lambda: self._hesapla(self._log10_hesapla)).grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.log_frame, text="log₂(x)", command=lambda: self._hesapla(self._log2_hesapla)).grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self.log_frame, text="Taban (b>0, b≠1):").grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.log_b_entry = ttk.Entry(self.log_frame, width=10)
        self.log_b_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Button(self.log_frame, text="log_b(x)", command=lambda: self._hesapla(self._logb_hesapla)).grid(row=3, column=1, pady=5)

        self.log_sonuc = ttk.Label(self.log_frame, text="Sonuç: ", font=("Arial", 10, "bold"))
        self.log_sonuc.grid(row=4, column=0, columnspan=3, pady=15)

    def _ln_hesapla(self):
        x = float(self.log_x_entry.get())
        return f"ln({x}) = {dogal_log(x):.6f}"

    def _log10_hesapla(self):
        x = float(self.log_x_entry.get())
        return f"log₁₀({x}) = {log10(x):.6f}"

    def _log2_hesapla(self):
        x = float(self.log_x_entry.get())
        return f"log₂({x}) = {log2(x):.6f}"

    def _logb_hesapla(self):
        x = float(self.log_x_entry.get())
        b = float(self.log_b_entry.get())
        return f"log_{b}({x}) = {log_b(x, b):.6f}"


    def _setup_istatistik_tab(self):
        ttk.Label(self.istatistik_frame, text="Veri (virgülle ayırın):").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        self.veri_entry = ttk.Entry(self.istatistik_frame, width=40)
        self.veri_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        ttk.Button(self.istatistik_frame, text="Ortalama", command=lambda: self._hesapla(self._ortalama_hesapla)).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(self.istatistik_frame, text="Medyan", command=lambda: self._hesapla(self._medyan_hesapla)).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(self.istatistik_frame, text="Mod", command=lambda: self._hesapla(self._mod_hesapla)).grid(row=2, column=2, padx=5, pady=5)
        ttk.Button(self.istatistik_frame, text="Std Sapma", command=lambda: self._hesapla(self._std_hesapla)).grid(row=3, column=1, pady=5)

        self.istatistik_sonuc = ttk.Label(self.istatistik_frame, text="Sonuç: ", font=("Arial", 10, "bold"))
        self.istatistik_sonuc.grid(row=4, column=0, columnspan=3, pady=15)

    def _parse_veri(self):
        veri_str = self.veri_entry.get().strip()
        if not veri_str:
            raise ValueError("Veri girilmemiş.")
        try:
            return [float(x.strip()) for x in veri_str.split(",")]
        except ValueError:
            raise ValueError("Geçersiz veri formatı. Sayıları virgülle ayırın (örn: 1,2,3).")

    def _ortalama_hesapla(self):
        veri = self._parse_veri()
        return f"Ortalama = {ortalama(veri):.4f}"

    def _medyan_hesapla(self):
        veri = self._parse_veri()
        return f"Medyan = {medyan(veri):.4f}"

    def _mod_hesapla(self):
        veri = self._parse_veri()
        sonuc = mod(veri)
        if isinstance(sonuc, list):
            return f"Mod = [{', '.join(map(str, sonuc))}]"
        else:
            return f"Mod = {sonuc}"

    def _std_hesapla(self):
        veri = self._parse_veri()
        return f"Standart Sapma = {standart_sapma(veri):.4f}"


    def _hesapla(self, fonksiyon):
        try:
            sonuc_metni = fonksiyon()
            # Hangi sekmedeyiz?
            current = self.notebook.index("current")
            if current == 0:
                self.trig_sonuc.config(text="Sonuç: " + sonuc_metni)
            elif current == 1:
                self.log_sonuc.config(text="Sonuç: " + sonuc_metni)
            else:
                self.istatistik_sonuc.config(text="Sonuç: " + sonuc_metni)
        except Exception as e:
            messagebox.showerror("Hata", f"Hesaplama hatası:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Matematik(root)
    root.mainloop()        
