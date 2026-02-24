def intersection(list1, list2):
    set1 = set(list1)   # Ubah ke set
    set2 = set(list2)

    hasil = list(set1 & set2)  # Operator & untuk irisan

    return hasil