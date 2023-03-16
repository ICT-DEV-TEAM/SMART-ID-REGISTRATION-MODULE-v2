import random

data = "test123"

set_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-)+=?/,:.<>_`~"

seed = 9

def create_cipher(seed):
    random.seed(seed)
    char_list = [letter for letter in set_1]
    return "".join(random.sample(char_list, k=len(char_list)))

def translate(text):
    new_text = str.maketrans(set_1, set_2)
    return text.translate(new_text)

def randomize_padding(padding_len, set_2):
    count = 0
    padding = []
    while count < padding_len:
        idx = random.randint(0, len(set_2) - 1)
        padding.append(set_2[idx])
        count += 1
    return "".join(padding)

def get_padding(set_2):
    padding_len = 5
    total_padding = 100
    padding = []
    for i in range(total_padding):
        padding.append(randomize_padding(padding_len, set_2))
    return padding

def insert_padding(string):
    padded_string = []
    for i in [x for x in string]:
        padded_string.append(i)
        for z in range(random.randint(1, 3)):
            padded_string.append(padding[random.randint(0, len(padding) - 1)])
    return "".join(padded_string)

def encrypt(data, filename):
    encrypted = insert_padding(translate(data))
    with open(filename, 'w') as file:
        file.write(encrypted)

set_2 = create_cipher(seed)

padding = get_padding(set_2)

encrypt(data, 'db_config.txt')



        