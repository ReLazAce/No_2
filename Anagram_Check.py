def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    hitung = {}

    for huruf in str1:
        hitung[huruf] = hitung.get(huruf, 0) + 1

    for huruf in str2:
        if huruf not in hitung:
            return False
        hitung[huruf] -= 1

    return all(nilai == 0 for nilai in hitung.values())