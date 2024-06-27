def ubah_huruf(text):
    shift = 10
    result = []
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Compute the encrypted character
            encrypted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            result.append(encrypted_char)
        else:
            # If it's not an alphabetic character, leave it as it is
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE"))     # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA"))       # SXNYXOCSK
    print(ubah_huruf("GOLANG"))          # QYVKXQ
    print(ubah_huruf("PROGRAMMER"))      # ZBYQBKWWOB
