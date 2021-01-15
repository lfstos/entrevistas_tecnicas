

def contar_letras(s: str):
    dct = {}
    for letra in s:
        dct[letra] = dct.get(letra, 0) + 1
    return dct

print(contar_letras('banana'))