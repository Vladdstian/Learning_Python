# Caesar cipher - encrypt and decode function creation
# Is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in
# which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For
# example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after
# Julius Caesar, who used it in his private correspondence.

def encrypt(message, shifter):
    new_message = ""
    for letter in message:
        result = alphabet.index(letter) + shifter
        if result > len(alphabet):
            result -= len(alphabet)
            new_message += alphabet[result]
        else:
            new_message += alphabet[result]
    print(new_message)


def decode(message, shifter):
    new_message = ""
    for letter in message:
        result = alphabet.index(letter) - shifter
        if result < 0:
            result += len(alphabet)
            new_message += alphabet[result]
        else:
            new_message += alphabet[result]
    print(new_message)


# list.index(value) gives the index of the value.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(message=text, shifter=shift)
else:
    decode(message=text, shifter=shift)
