alphabet = list('abcdefghijklmnopqrstuvwxyz')
direction = input("Enter 'encode' to encrypt, or 'decode' to decrypt: ")
text = input("Enter the message: ").lower()
shift = int (input("Enter the shift value: "))


code = []


def fun_encode(text,alphabet,shift):
    for l in range(len(alphabet)):
        for letter in text:

            if letter in alphabet:
                    code.append(alphabet[l+shift])
    encode="".join(code)
    print(encode)

def fun_decode(text,alphabet,shift):
    for l in range(len(alphabet)):
        for letter in text:
            if letter in alphabet:
                code.append(alphabet[l-shift])
    decode="".join(code)
    print(decode)

if direction == "encode":
    fun_encode(text,alphabet,shift)
elif direction == "decode":
    fun_decode(text,alphabet,shift)
else:
    print("Invalid input")
