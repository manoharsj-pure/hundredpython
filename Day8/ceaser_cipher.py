

def encrypt( input_string , encryption_key ):
    encrypted_string= []
    for each_letter in input_string:
        if ( each_letter == " "):
            encrypted_string.append(" ")
            continue
        current_index=alphabets.index(each_letter) + 1
        new_index= ( current_index % 26 ) + int(encryption_key) - 1
        encrypted_string.append(alphabets[new_index])
    return (encrypted_string)

def decrypt( input_string , decryption_key ):
    decrypted_string = []
    for each_letter in input_string:
        if each_letter == " " :
            decrypted_string.append(" ")
            continue
        new_index=alphabets.index(each_letter) - int(decryption_key)
        new_index = new_index % len(alphabets)
        #current_index = alphabets.index(each_letter) + 1
        #new_index= (( current_index % 26 ) - int(decryption_key) - 1)
        decrypted_string.append(alphabets[new_index])
    return (decrypted_string)


alphabets=['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l', 'm' , 'n' , 'o' , 'p' , 'q', 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']
input_string=input("Enter the Original Message: ")
encrypt_key=input("Enter the Encryption Key: ")

encrypted_string=encrypt(input_string , encrypt_key )
print("Here is the encrypted string:  " + ''.join(encrypted_string))

decrypted_string=decrypt( ''.join(encrypted_string) , encrypt_key)
print("Here is the decrypted string:  " + ''.join(decrypted_string))


