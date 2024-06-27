# Problem 1 - Play With Asterisk
def play_with_asterisk(n):
    result = ""
    for i in range(1, n + 1):
        result += ' ' * (n - i) + '* ' * i + '\n'
    return result

def main():
    try:
        num = int(input("Masukkan jumlah baris: "))
        if num > 0:
            print(play_with_asterisk(num))
        else:
            print("Masukkan bilangan positif.")
    except ValueError:
        print("Input harus berupa bilangan bulat.")

# karena inputnya 5 maka
print(play_with_asterisk(5))