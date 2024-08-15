# verificar se uma senha está nos padrões recomendados
import re

print("#" * 50)
print("#")
print("#        Password check      ")
print("#")
print("#" * 50)

cont = str(input("Digite 'S' para continuar: "))
if cont == "s" or "s".upper:
    pwd_user = str(input("Digite uma senha que tenha pelo menos 12 caracteres, sendo eles 2 letras maiusculas, numeros e caracteres especiais:"))

while not pwd_user (re.search(r'.{12,}', pwd_user) and
                    re.search(r'[A-Z]', pwd_user) and
                    re.search(r'\d', pwd_user) and
                    re.search(r'[!@#$%¨&*]', pwd_user)):
    pwd_user = input("Sua senha está correta")
    print(pwd_user)