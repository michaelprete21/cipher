alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_char = alphabet[new_position]
        else:
            new_char = char
        end_text += new_char

    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo

print(logo)

while True:
    while True:
        direction = input(
            "\nType 'encode' to encrypt or type 'decode' to decrypt:\n")
        if direction == 'decode' or direction == 'encode':
            break
        else:
            print("\nPlease enter valid input.\n")
            continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26

    cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    cont = input(
        "\n\nWould you like to encode or decode another statement? Enter yes or no:\n").lower()
    if cont == "no":
        break
    else:
        continue