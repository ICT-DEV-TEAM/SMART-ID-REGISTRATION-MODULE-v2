from encrypt import set_1, create_cipher, get_padding

def remove_padding(string, set_2):
    padding = get_padding(set_2)
    for i in padding:
        if i in string:
            string = string.replace(i, '')
    return string

def retranslate(set_1, set_2, string):
    new_text = str.maketrans(set_2, set_1)
    return string.translate(new_text)

def decrypt(string, seed):
    set_2 = create_cipher(seed)
    decrypted = ''
    decrypted = retranslate(set_1, set_2, remove_padding(string, set_2))
    return decrypted