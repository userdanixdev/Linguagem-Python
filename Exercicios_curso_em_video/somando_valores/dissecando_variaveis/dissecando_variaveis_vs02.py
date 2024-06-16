

while True:
    algo = input('Digite algo: ')
    if algo.isspace():
        print('Apenas espaços, dado incorreto')
    if algo.isnumeric():
        print('é número')
    if algo.isalpha():
        print('é letra')
    if algo.isalnum():
        print('é Alfanumérico')
    if algo.islower():
        print('letras minusculas')
    if algo.istitle():
        print('capitalizada')
    if algo.isupper():
        print('maiusculas')
