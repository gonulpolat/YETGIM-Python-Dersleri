"""
    **Frekans Analizi**: Bir metindeki kelimelerin sıklığını bulan program
"""

metin = """
        On it differed repeated wandered required in. Then girl neat why yet knew rose spot. Moreover property we he kindness greatest be oh striking laughter. In me he at collecting affronting principles apartments. Has visitor law attacks pretend you calling own excited painted. Contented attending smallness it oh ye unwilling. Turned favour man two but lovers. Suffer should if waited common person little oh. Improved civility graceful sex few smallest screened settling. Likely active her warmly has.

        Breakfast procuring nay end happiness allowance assurance frankness. Met simplicity nor difficulty unreserved who. Entreaties mr conviction dissimilar me astonished estimating cultivated. On no applauded exquisite my additions. Pronounce add boy estimable nay suspected. You sudden nay elinor thirty esteem temper. Quiet leave shy you gay off asked large style.

        In it except to so temper mutual tastes mother. Interested cultivated its continuing now yet are. Out interested acceptance our partiality affronting unpleasant why add. Esteem garden men yet shy course. Consulted up my tolerably sometimes perpetual oh. Expression acceptance imprudence particular had eat unsatiable.
        """

import string

# print(metin.split())
# print(string.punctuation)
# temiz_metin = metin.translate(str.maketrans("", "", string.punctuation))
# print(temiz_metin)

sozluk = dict()
def frequency(txt: str) -> dict:
    txt = txt.translate(str.maketrans("", "", string.punctuation)).lower()
    for word in txt.split():
        if word in sozluk:
            sozluk[word] += 1
        else:
            sozluk[word] = 1

    return sozluk

result = frequency(metin)
print(result)
