# Problem 2 - Draw XYZ
def draw_xyz(N):
    result = ""
    for i in range(1, N * N + 1):
        if i % 3 == 0:
            result += "X "
        elif i % 2 == 0:
            result += "Z "
        else:
            result += "Y "
        
        if i % N == 0:
            result += "\n"  # Pindah ke baris berikutnya setelah mencetak N elemen
    return result

# Main program to test the function
def main():
    try:
        num = int(input("Masukkan nilai N: "))
        if num > 0:
            print(draw_xyz(num))
        else:
            print("Masukkan bilangan positif.")
    except ValueError:
        print("Input harus berupa bilangan bulat.")

# Karena inputnya sama dengan 3
print(draw_xyz(3))
# Karena inputnya sama dengan 5
print(draw_xyz(5))