

alphabet = list('abcdefghijklmnopqrstuvwxyz')
should_continue = True
while should_continue:
    direction = input("Enter 'encode' to encrypt, or 'decode' to decrypt: ")
    while direction != "encode" and direction != "decode":
        direction=input("Invalid direction, Enter 'encode' to encrypt, or 'decode' to decrypt: ").lower()
    text = input("Enter the message: ").lower()
    shift = int (input("Enter the shift value: "))



    def encrypt(start_text,shift_amount,cipher_direction):
        code = ""


        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)

                if cipher_direction == 'decode':
                    shift_amount = shift_amount * -1
                    shift_amount = shift_amount

                new_position = position + shift_amount

                code+=(alphabet[new_position% 25])
            else:
                code+=letter
        print(code)

    encrypt(start_text=text,shift_amount=shift,cipher_direction=direction)
    response = input("Do you wanna go again?y/n").lower()
    if response == "n":
        should_continue = False
