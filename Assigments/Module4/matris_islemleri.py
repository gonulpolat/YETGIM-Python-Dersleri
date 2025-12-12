"""
    **Matris İşlemleri**: Matris toplama, çıkarma, çarpma programı
"""

def _degerleri_getir(m1, m2):
    row = len(m1)
    column = len(m1[0])
    return row, column

def matris_topla(m1, m2):
    row, column = _degerleri_getir(m1, m2)
    result = []
    for i in range(row):
        new_row = []
        for j in range(column):
            toplam = m1[i][j] + m2[i][j]
            new_row.append(toplam)
        result.append(new_row)
    
    return result


def matris_cikar(m1, m2):
    row, column = _degerleri_getir(m1, m2)
    result = []
    for i in range(row):
        new_row = []
        for j in range(column):
            fark = m1[i][j] - m2[i][j]
            new_row.append(fark)
        result.append(new_row)
    
    return result


def matris_carp(m1, m2):
    row, column = _degerleri_getir(m1, m2)
    result = []
    for i in range(row):
        new_row = []
        for j in range(column):
            carpim = 0
            for k in range(len(m1[0])):  # diğer matrise göre de olabilir
                carpim += m1[i][k] * m2[k][j]
            new_row.append(carpim)
        result.append(new_row)
    
    return result



if __name__ == "__main__":

    A = [
        [1, 2, 3],
        [4, 5, 6],
        [1, 7, 8],
    ]

    B = [
        [8, 5, 3],
        [1, 9, 9],
        [2, 3, 2],
    ]

    print(matris_topla(A, B))
    print(matris_cikar(A, B))
    print(matris_carp(A, B))
