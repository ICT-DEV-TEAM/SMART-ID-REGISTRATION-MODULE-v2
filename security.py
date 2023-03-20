import encrypt as enc
import decrypt as dec

filename = 'db_config.txt'

def save_to_file(filename, string):
    with open(filename, 'w') as file:
        file.write(string)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def encrypt(data, filename, delimiter):
    join_data = delimiter.join(data)
    to_encrypt = enc.encrypt(join_data)
    try:
        dec.decrypt(to_encrypt)
        save_to_file(filename, to_encrypt)
    except:
        reencrypt = enc.encrypt(to_encrypt)
        save_to_file(filename, reencrypt)

def decrypt(filename, delimiter):
    raw_string = read_file(filename)
    to_decrypt = dec.decrypt(raw_string)
    actual_config = to_decrypt.split(delimiter)
    return actual_config

# data = ['localhost','root','','smart_id','3306']
# encrypt(data=data, filename='db_config.txt', delimiter='!')