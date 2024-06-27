def cetak_tabel_perkalian(n):
    result = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += f"{i * j:2} "
        result = result.rstrip() + " \n"  # Menambahkan spasi dan pindah ke baris berikutnya
    return result
