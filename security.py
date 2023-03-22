import encrypt as enc
import decrypt as dec
import time

filename = 'db_config.txt'
insert_seed = '!@@:#!aQw'

def save_to_file(filename, string):
    with open(filename, 'w') as file:
        file.write(string)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def encrypt(data, filename, delimiter):
    while True:
        join_data = delimiter.join(data)
        to_encrypt = enc.encrypt(join_data)
        to_encrypt += insert_seed + enc.seed
        try:
            seed = to_encrypt.split(insert_seed)[-1]
            dec.decrypt(to_encrypt, seed)
            save_to_file(filename, to_encrypt)
            print('encrypted')
            break
        except Exception as e:
            print(e)
            continue

def decrypt(filename, delimiter):
    raw_string = read_file(filename)
    seed = raw_string.split(insert_seed)[-1]
    raw_string = raw_string.split(insert_seed)[0]
    to_decrypt = dec.decrypt(raw_string, seed)
    actual_config = to_decrypt.split(delimiter)
    return actual_config

if __name__ == '__main__':
    data = ['localhost','root','','smart_id','3306']
    encrypt(data=data, filename='db_config.txt', delimiter='!')
    print(decrypt(filename=filename, delimiter='!'))  