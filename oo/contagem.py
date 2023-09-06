import nome


def contar_caracteres(nome):

caracteres_ordenados = sorted(nome)
caracter_anterior = caracteres_ordenados[0]
contagem = 1

for caracter in caracteres_ordenados[1:]:
    if caracter == caracteres_ordenados:
        contagem += 1
    else:
        print(f'{caracter_anterior}: {contagem}')
        caracter_anterior = caracter
        contagem = 1

print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('Jardel')
    print()
    contar_caracteres('Rebouças')
