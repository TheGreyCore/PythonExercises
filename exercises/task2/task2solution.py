def korrutaKahega(massiiv):
    return massiiv


def teisendaSõneTäisArvuks(sõne):
    return sõne


def testid():
    assert korrutaKahega([1, 2, 3]) == [2, 4, 6]
    assert korrutaKahega(["üks", "kaks", "üheksa"]) == [2, 4, 18]
    assert korrutaKahega([2, "kaks", 9]) == [4, 4, 18]
    assert korrutaKahega([]) == []
    print("Kõik testid läbisid edukalt!")


if __name__ == "__main__":
    massiiv = [64, 34, 25, 12, 22, 11, 90]
    print(korrutaKahega(massiiv))
    testid()