import pyfiglet

#Note: This was made with loose guidence of this tutorial: 
#http://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

#logo for aesthetics:
pyfiglet.print_figlet("CaesarCipher.py", colors='GREEN')
print("By Steven")

#Encrypt a string:

def ccEncrypt(plnTxt, shift):
    result = ''

    for a in range(len(plnTxt)):
        char = plnTxt[a]

        #Upper Case:
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        
        #Lower Case
        else:
            result += chr((ord(char) + key-97) % 26 + 97)
    
    return result

#Decrypt a String: (Literally encrypt but swap the + signs for - signs lol)

def ccDecrypt(plnTxt, shift):
    result = ''

    for a in range(len(plnTxt)):
        char = plnTxt[a]

        #If Upper Case:

        if (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
        
        #Lower Case
        else:
            result += chr((ord(char) - key-97) % 26 + 97)
    
    return result

ans1 = "1"
ans2 = "2"

print("Would you like to 1.) Encrypt or 2.) Decrypt")

EorD = input(">>")

if EorD in ans1:

#Code for Encrypt:
    print("Input a Key: ")
    key = int(input(">>"))

    print("Input a String: ")
    plnTxt = input(">>")

    print("Original: ", plnTxt)
    print("Shift: " + str(key))
    print("Encrypted: " + ccEncrypt(plnTxt,key))

if EorD in ans2:

#Code for Decrypt:
    print("Input a Key: ")
    key = int(input(">>"))

    print("Input a String: ")
    plnTxt = input(">>")

    print("Original: ", plnTxt)
    print("Shift: " + str(key))
    print("Decrypted: " + ccDecrypt(plnTxt,key))

else:
    exit



   



