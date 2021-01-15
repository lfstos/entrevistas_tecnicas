def retorna_frase_invertida(frase: str):
    '''
    2) Crie uma função que retorna todas as palavras de uma string:
    Exemplo: fn("A frase inteira deve ser revertida") -> "revertida ser deve inteira frase a"

    :param frase:
    :return:
    '''

    frase = frase.split(' ')

    return ' '.join(frase[::-1])

print(retorna_frase_invertida("A frase inteira deve ser revertida"))