import random as rand
import decryptData as dec

syl = ["y1Ct6", "v6pWd", "gU0aK", "O4Erl", "o8PjF", "G5iRc", "S3wLd", "x5Qh0", "b4nDp", "m9XoJ", "f5xGh", "q3ZcS", "K8nVj", "L1hNv", "Y2Wjz", "N6iPu", "U1jHd", "z7OcI", "T6vLd", "s8FgK", "D1eJo", "Q2wPf", "M3yKg", "k7XrJ", "B1fRn", "I6tPc", "r8JnV", "j3qLu", "E9mZs", "t0cRb", "Z7kNw", "u9fTp", "a6IhV", "W8sGx", "C1tNf", "H2wLu", "p5OcD", "F9vXe", "d4BhJ", "i6Tfz", "n8EwR", "y4MjS", "X5kUq", "l2QoP", "A3sZd", "e7VcF", "b1YmK", "o9FjG", "g5IuN", "w6LpT"]


def randomElement():
    pos = rand.randint(0,len(syl) - 1)
    return syl[pos]


def encrypt(singleCharacter):
    return f"{randomElement()}{hex(ord(singleCharacter))}"


def encodeWithOrd(txt):
    encryptedTxt = ""
    for character in txt:
        encryptedTxt += encrypt(character)
    return encryptedTxt


def reEncodeWithoutOrd(plainTxt):
    encryptedTxt = ""
    for character in encodeWithOrd(plainTxt):
        encryptedTxt += f"{randomElement()}{character}"
    return encryptedTxt


def generate(plainTxt):
    while True:
        encryptedStr = reEncodeWithoutOrd(plainTxt)
        try: 
            decrptedStr = dec.decryptStr(encryptedStr)
            if plainTxt == decrptedStr:
                break
        except Exception:
            continue
    return encryptedStr

