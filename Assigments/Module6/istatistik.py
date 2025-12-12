import statistics

def ortalama(veri): return statistics.mean(veri)

def medyan(veri): return statistics.median(veri)

def mod(veri):
    """
    En sık tekrar eden değeri döner.
    Birden fazla mod varsa hepsini döner.
    """
    try:
        return statistics.mode(veri)
    except statistics.StatisticsError:
        return statistics.multimode(veri) if hasattr(statistics, 'multimode') else "Mode Yok"
    
def standart_sapma(veri):
    if len(veri) < 2:
        raise ValueError("Standart sapma hesaplamak için en az 2 veri gerekir.")
    return statistics.stdev(veri)
