def fizz_buzz(n: int):
    '''
    Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
    Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
    Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.


    :param n:
    :return:
    '''

    for i in range(1, n + 1): # i=[1, 2, 3, 4, 5, 6]
        resultado = ''
        if i % 3 == 0:
            resultado = 'fizz'
        if i % 5 == 0:
            resultado += 'buzz'
        resultado = resultado if resultado != '' else i # resultado=[1, 2, fizz, 4, buzz, ]
        print(resultado)


fizz_buzz(15)