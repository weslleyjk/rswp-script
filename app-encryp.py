# Weslley Felix - Projeto Python
import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()
with open("chave.key", "wb") as chave_encrypt:
     chave_encrypt.write(key)

with open("chave.key", "rb") as chave_encrypt:
    key = chave_encrypt.read()

# Criar o objeto Fernet
fernet = Fernet(key)

diretorio = ""  
nome_arquivo = "teste-criptografia.txt"
filepath = os.path.join(diretorio, nome_arquivo)

if os.path.exists(filepath):
    with open(filepath, 'rb') as arquivo:
        dados = arquivo.read()
        
    dados_criptografados = fernet.encrypt(dados)
    
    # Salvar o arquivo criptografado
    with open(filepath + '.enc', 'wb') as file_criptografado:
        file_criptografado.write(dados_criptografados)
    
    # Remover o arquivo original
    os.remove(filepath)
    print(f"Arquivo {nome_arquivo} criptografado com sucesso.")
else:
    print(f"O Arquivo {nome_arquivo} não existe no diretório especificado")