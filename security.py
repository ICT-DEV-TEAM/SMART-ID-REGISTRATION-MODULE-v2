import encrypt as enc
import decrypt as dec

filename = 'db_config.txt'

data = 'test/data::abc123'

def save_to_file(filename, string):
    with open(filename, 'w') as file:
        file.write(string)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def encrypt(data, filename):
    to_encrypt = enc.encrypt(data)
    try:
        dec.decrypt(to_encrypt)
        save_to_file(filename, to_encrypt)
    except:
        reencrypt = enc.encrypt(to_encrypt)
        save_to_file(filename, reencrypt)

def decrypt(filename):
    to_decrypt = read_file(filename)
    return dec.decrypt(to_decrypt)

encrypt(data, filename)
