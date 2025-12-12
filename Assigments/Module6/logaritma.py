import math

def _is_validate(x):
    if x <= 0:
        raise ValueError("Logartima girdisi pozitif olmalıdır.")


def dogal_log(x):
    """
    ln(x) = e tabanında logaritma
    """
    _is_validate(x)
    return math.log(x)

def log10(x):
    """
    10 tabanında logaritma    
    """
    _is_validate(x)
    return math.log10(x)

def log2(x):
    """
    2 tabanında logaritma
    """
    _is_validate(x)
    return math.log2(x)

def log_b(x, b):
    """
    b tabanında logaritma => log_b(x)
    """
    _is_validate(x)
    if b <= 0 or b == 1:
        raise ValueError("Geçersiz logaritma tabanı")
    return math.log(x) / math.log(b)
