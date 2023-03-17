import encrypt as enc

def remove_padding(string):
    for i in enc.padding:
        if i in string:
            string = string.replace(i, '')
    return string

def retranslate(set_1, set_2, string):
    new_text = str.maketrans(set_2, set_1)
    return string.translate(new_text)

def decrypt(string):
    decrypted = ''
    decrypted = retranslate(enc.set_1, enc.set_2, remove_padding(string))
    return decrypted
