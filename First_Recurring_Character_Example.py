def first_recurring(text):
    sudah_ada = set()

    for huruf in text:
        if huruf in sudah_ada:
            return huruf
        sudah_ada.add(huruf)

    return None

print(first_recurring("abca"))