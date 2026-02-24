def intersection(list1, list2):
    set1 = set(list1)   # Ubah ke set
    set2 = set(list2)

    hasil = list(set1 & set2)  # Operator & untuk irisan

    return hasil

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(intersection(a, b))