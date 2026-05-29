# %%
# atribui o arquivo de texto 'historia.txt' à variável 'nome_arquivo'
nome_arquivo = "historia.txt"

#%%
# Abre arquivo em formato de leitura
open_file = open(nome_arquivo)

# Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

#%%
# fecha o arquivo para garantir que ele possa ser alterado e não corrompa o próprio arquivo
open_file.close()


#%%

# A forma mais usual para ler arquivos em Python

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)
