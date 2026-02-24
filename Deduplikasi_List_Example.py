def deduplikasi(data):
    hasil = []          # List untuk menyimpan hasil tanpa duplikat
    sudah_ada = set()   # Set untuk melacak elemen yang sudah muncul

    for item in data:
        if item not in sudah_ada:   # Jika belum pernah muncul
            hasil.append(item)      # Tambahkan ke hasil
            sudah_ada.add(item)     # Tandai sebagai sudah muncul

    return hasil

data = [1, 2, 2, 3, 4, 3, 5]
print(deduplikasi(data))