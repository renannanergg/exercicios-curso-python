palavras= ('aprender',
           'programar',
           'linguagem',
           'computador',
           'futuro',
           'praticar',
           'trabalhar',
           'estudar',
           'progresso')
for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem ',end='')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')