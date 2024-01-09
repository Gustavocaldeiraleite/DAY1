def count(days):
    days *= 365
    return days
while True:
    try:
        age = int(input('digite sua idade'))
        if age > 0:
            break
        else:
            print('idade deve ser positiva')
    except ValueError:
        print('Erro, digite uma idade valida')
print(f'quantidade de dias que voce viveu foi de {count(age)}')