try:

    def saitama():
        genos = goku()
        genos = str(genos)
        return genos

    def light():
        ryuk = gon()
        l = ryuk.split("A1")
        l.remove("")
        return l
    
    def goku():
        gohan = open(f"DY.txt", "r")
        chichi = gohan.read()
        return chichi

    def kaneki():
        touka = light()
        rize = ""
        for suzuya in touka:
            rize += f"{chr(int(suzuya, 16))}"
        return rize

    def gon():
        killua = ["Dy", "aR" , "Bu" , "fC" , "Pc" , "pY" , "To" ]
        kurapika = saitama()
        for hisoka in killua:
            kurapika = kurapika.replace(hisoka, "A1")
        return kurapika

except Exception:
    pass
