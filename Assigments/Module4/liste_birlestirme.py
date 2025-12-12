"""
    **Liste Birleştirme**: İki sıralı listeyi birleştiren program (merge sort mantığı)
"""


def liste_birlestir(liste1: list, liste2: list) -> list:
    merged = []
    i, j = 0, 0  # pointers

    while i < len(liste1) and j < len(liste2):
        if liste1[i] <= liste2[j]:
            merged.append(liste1[i])
            i += 1
        else:
            merged.append(liste2[j])
            j += 1

    while i < len(liste1):
        merged.append(liste1[i])
        i += 1

    while j < len(liste2):
        merged.append(liste2[j])
        j += 1
    return merged


if __name__ == "__main__":
    liste1 = [1, 4, 8, 12]
    liste2 = [2, 5, 6, 18, 20, 21]
    result = liste_birlestir(liste1, liste2)
    print(result)
