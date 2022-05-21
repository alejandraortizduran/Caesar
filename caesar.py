import sys

def caesar(args):
    s=args
    result = ""
    text = input('plaintext : ')

    for i in range(len(text)):
        char = text[i]

            # Uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65) if (char != ',') else char

            # Lowercase characters
        else:
            if (char == ' '):
                result +=char
            elif (char == ','):
                result +=char
            else:
                result += chr((ord(char) + s - 97) % 26 + 97) 

    print ("ciphertext : " + result)
    return

if(len(sys.argv)==2):
    n=int(sys.argv[1])
    caesar(n)
else:
    print('Invalid number of arguments')
    exit()
    
   
    



