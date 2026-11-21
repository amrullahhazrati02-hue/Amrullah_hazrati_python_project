def encrypt(orignal_text,shift_amount):
    output_text=""
    for letter in orignal_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position = alphabet.index(letter)+shift_amount
            shifted_position %= len(alphabet)
            output_text+=alphabet[shifted_position]

        print(f'Here is the encode result: {output_text}')

def decrypt(orignal_text,shift_amount):
    output_text=""
    for letter in orignal_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position %= len(alphabet)
            output_text = output_text - alphabet[shifted_position]
            print(f'Here is the decrypt result: {output_text}')