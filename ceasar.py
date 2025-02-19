import cryptography
import string

# creating substitution tables

def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)

    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding


# creating shift encoder
def encode(message, subst):
    cipher = ""
    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    return cipher


def decode(message, subst):
    return encode(message, subst)


# printable substitutions

def printable_substitution(subst):

    # sort by source character so things are alphabetized
    mapping = sorted(subst.items())
    
    # then create two lines: source above, target beneath
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line =  " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cipher_line)


# Shift Cipher Application


if __name__ == "__main__":
    n = 1
    encoding, decoding = create_shift_substitutions(n)
    while True:
        print("\n Shift Encoder Decoder")
        print("--------------------------")
        print("\t Current Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode MEssage.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">>")
        print()


        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\n  Message to encode: ")
            print("Encoded Message: {}".format(
                encode(message.upper(), encoding)
            ))

        elif choice == '3':
            message = input("\n Message to decode:")
            print("Decoded Message: {}".format(decode(message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\n New Shift (currently {}):".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions(n)

        elif choice == '5':
            print("Terminating. This program will self destruct in 5 seconds. \n")
            break
        else:
            print("Umknown option {}.".format(choice))