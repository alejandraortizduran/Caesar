import sys

def caesar(n):
    code = ""
    text = input('plaintext : ')

    for i in range(len(text)):
        c = text[i]

            # Uppercase characters
        if (c.isupper()):
            code += chr((ord(c) + n-65) % 26 + 65)

            # Lowercase characters
        else:
            if (c == ' '):
                code +=c
            elif (c == ','):
                code +=c
            else:
                code += chr((ord(c) + n - 97) % 26 + 97) 

    print ("ciphertext : " + code)
    return

if(len(sys.argv)==2):
    n=int(sys.argv[1])
    caesar(n)
else:
    print('Invalid number of arguments')
    exit()
