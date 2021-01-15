def maior_numero_impar(n: int):
    '''
    1) Crie uma função que retorn o maior número ímpar da sequencia (sem usar max).

    Exemplo: fn([1,2,3,4,5,6,7,8,9,10,11,12,14,16]) -> 11

    :param n:
    :return:
    '''

    impar = []

    for i in n:
        if i % 2 != 0:
            impar.append(i)
    return sorted(impar)[-1]

print(maior_numero_impar([1,2,3,4,5,6,7,8,9,10,11,12,14,16]))