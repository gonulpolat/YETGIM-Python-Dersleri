import math

# yardımcı fonksiyon (uygulama içi fonksiyon)
def _is_validate(value, min_value=-1, max_value=1):
    if not (min_value <= value <= max_value):
        raise ValueError(f"Girdi [{min_value}, {max_value}] aralığında olmalıdır.")

def derece_to_radyan(derece: int) -> float:
    """
    Dereceyi radyana çevirir
    :param derece: 
    :type derece: int
    :return: 
    :rtype: float
    """
    return math.radians(derece)


def radyan_to_derece(radyan: int) -> float:
    """
    Radyanı dereceye çevirir
    :param radyan: 
    :type radyan: int
    :return: 
    :rtype: float
    """
    return math.degrees(radyan)


def sin_derece(derece: int) -> float:
    """
    Derece cinsinden sinüs hesaplar
    :param derece: Reel sayılar
    :type derece: int
    :return: [-1, 1] aralığında sonuç
    :rtype: float
    """
    return math.sin(derece_to_radyan(derece))


def cos_derece(derece: int) -> float:
    """
    Derece cinsinden kosinüs hesaplar
    :param derece: Reel sayılar
    :type derece: int
    :return: [-1, 1] aralığında sonuç
    :rtype: float
    """
    return math.cos(derece_to_radyan(derece))


def tan_derece(derece: int) -> float:
    """
    Derece cinsinden tanjant hesaplar
    :param derece: 
    :type derece: int
    :return: Reel sayılar
    :rtype: float
    """
    radyan = derece_to_radyan(derece)
    if abs(math.cos(radyan)) < 1e-10:
        print(f"Uyarı: tan({derece}) tanımsıza yakındır.")
    return math.tan(radyan)


def arcsin_derece(deger: int) -> float:
    """
    Girilen değerin arcsin'ini derece cinsinden hesaplar
    :param deger: [-1, 1] aralığında değer
    :type deger: int
    :return: [-90, 90] aralığında sonuç
    :rtype: float
    """
    _is_validate(deger, -1, 1)
    return radyan_to_derece(math.asin(deger))


def arccos_derece(deger: int) -> float:
    """
    Girilen değerin arccos'unu derece cinsinden hesaplar
    :param deger: [-1, 1] aralığında değer
    :type deger: int
    :return: [-90, 90] aralığında sonuç
    :rtype: float
    """
    _is_validate(deger, -1, 1)
    return radyan_to_derece(math.acos(deger))


def arctan_derece(deger: int) -> float:
    """
    Girilen değerin arctan'ını derece cinsinden hesaplar
    :param deger: Reel sayılar
    :type deger: int
    :return: (-90, 90) aralığında değer
    :rtype: float
    """
    return radyan_to_derece(math.atan(deger))
