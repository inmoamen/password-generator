import random
import string

def gerar_senha (comprimento):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha
comprimento = int(input("digite o numero de caracteres"))
senha_gerada = gerar_senha(comprimento)
print("a senha gerada é:   ",senha_gerada)