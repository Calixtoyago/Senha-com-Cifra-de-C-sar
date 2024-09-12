import string, random

maiuscula = (string.ascii_uppercase)
minuscula = (string.ascii_lowercase)
digitos = (string.digits)

senha = []
nova_senha = []
quantidade = 8

# Gerador de senha aleatória
qnt_maiuscula = random.randint(1, (quantidade - 2))
qnt_numeros = random.randint(1, (quantidade - qnt_maiuscula - 1))
qnt_minuscula = quantidade - qnt_numeros - qnt_maiuscula

for c in range(qnt_maiuscula):
    senha.append(random.choice(maiuscula))
for c in range(qnt_numeros):
    senha.append(random.choice(digitos))
for c in range(qnt_minuscula):
    senha.append(random.choice(minuscula))
random.shuffle(senha)

def cifraCesar(senha):
    # Caso Base
    if len(senha) == 0:
        return nova_senha
    
    # Para dígitos
    if senha[0] in digitos:
        posicao = digitos.index(senha[0])
        if (posicao + 3) >= len(digitos):
            posicao = (posicao + 3) - len(digitos)
            nova_senha.append(digitos[posicao])
        else:
            nova_senha.append(digitos[posicao + 3])

    # Para letras maiúsculas
    elif senha[0] in maiuscula:
        posicao = maiuscula.index(senha[0])
        if (posicao + 3) >= len(maiuscula):
            posicao = (posicao + 3) - len(maiuscula)
            nova_senha.append(maiuscula[posicao])
        else:
            nova_senha.append(maiuscula[posicao + 3])

    # Para letras minúsculas
    elif senha[0] in minuscula:
        posicao = minuscula.index(senha[0])
        if (posicao + 3) >= len(minuscula):
            posicao = (posicao + 3) - len(minuscula)
            nova_senha.append(minuscula[posicao])
        else:
            nova_senha.append(minuscula[posicao + 3])

    # Responsividade
    return cifraCesar(senha[1:])

# Mostrar senha original
print(''.join(senha))

# Mostrar senha criptografada
resultado = cifraCesar(senha)
print(''.join(resultado))
