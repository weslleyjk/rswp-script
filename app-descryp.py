# Weslley Felix - Projeto Python

import os
from cryptography.fernet import Fernet


with open("chave.key", "rb") as chave_encrypt:
    key = chave_encrypt.read()

fernet = Fernet(key)

diretorio = ""
nome_arquivo = "teste-criptografia.txt.enc"
filepath_enc = os.path.join(diretorio, nome_arquivo)

if os.path.exists(filepath_enc):
    
    with open(filepath_enc, 'rb') as file:
        dados_criptografados = file.read()
    
    dados_criptografados = fernet.decrypt(dados_criptografados)
    
    novo_nome_arquivo = os.path.splitext(filepath_enc)[0] # remove a extensão .enc
    with open(novo_nome_arquivo, 'wb') as file_descriptografado:
        file_descriptografado.write(dados_criptografados)
        
        
    # Remover o arquivo criptografado
    os.remove(filepath_enc)
    print(f"Arquivo '{nome_arquivo}' descriptografado com sucesso.")
else:
    print(f"O arquivo criptografado '{nome_arquivo}' não existe no diretório especificado.")