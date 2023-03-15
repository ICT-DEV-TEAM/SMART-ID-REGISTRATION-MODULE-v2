
syl = ["y1Ct6", "v6pWd", "gU0aK", "O4Erl", "o8PjF", "G5iRc", "S3wLd", "x5Qh0", "b4nDp", "m9XoJ", "f5xGh", "q3ZcS", "K8nVj", "L1hNv", "Y2Wjz", "N6iPu", "U1jHd", "z7OcI", "T6vLd", "s8FgK", "D1eJo", "Q2wPf", "M3yKg", "k7XrJ", "B1fRn", "I6tPc", "r8JnV", "j3qLu", "E9mZs", "t0cRb", "Z7kNw", "u9fTp", "a6IhV", "W8sGx", "C1tNf", "H2wLu", "p5OcD", "F9vXe", "d4BhJ", "i6Tfz", "n8EwR", "y4MjS", "X5kUq", "l2QoP", "A3sZd", "e7VcF", "b1YmK", "o9FjG", "g5IuN", "w6LpT"]


def removeSym(encryptedStr):
    for syllable in syl:
        encryptedStr = encryptedStr.replace(syllable, "")
    return encryptedStr

def decryptStr(encryptedStr):
    plainTxt = ''
    noExtraSyl = removeSym(encryptedStr)
    for syllable in syl:
        noExtraSyl = noExtraSyl.replace(syllable, "Arjanel")
    letters = noExtraSyl.split("Arjanel")
    letters.remove("")
    
    for item in letters:
        plainTxt += f"{chr(int(item, 16))}"
    
    return plainTxt
    
