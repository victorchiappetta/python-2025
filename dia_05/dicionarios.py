# %%

lista = [2, 132, "teo", ["ds", "de", "da"], True]

lista[2]

# %%

# pares de chave/valor

dados_teo = {
    "sobrenome":"Calvo",
    "nome":"Téo", 
    "filhos":True,
    "formacao":["estatística", "bigdata datascience"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "sas" },
        {"nome": "ds sr.", "empresa": "boticario"},
        {"nome": "ds espec.", "empresa": "via varejo"},
    ]
}

# %%
print(dados_teo)

print(dados_teo["formacao"][-1]) # acessa a chave 'formacao' e pega o último valor, que nesse caso é 'bigdata datascience'
print(dados_teo["cargos"][-1]["empresa"]) # acessa a chave 'cargos', pega o último valor e depois acessa a chave 'empresa

# %%

# adiciona uma chave nova e dá um valor a ela
dados_teo["estado civil"] = "casado"
print(dados_teo)

# %%

# retorna uma lista das chaves de 'dados_teo'
print("Chaves:", dados_teo.keys())

# retorna uma lista dos valores de 'dados_teo'
print("Valores:", dados_teo.values())

# retorna uma lista de tuplas dos pares chave -> valor de 'dados_teo'
print("Items:", dados_teo.items())


# %%

for i in [10,20,45,28,"Téo"]:
    print(i)

# %%

# percorre o dict 'dados_teo', onde i == chave e dados_teo[i] retorna o valor dessa chave
for i in dados_teo:
    print(i, "->", dados_teo[i])

# %%

# igual ao anterior, mas de uma forma mais visual para entender chave -> valor
for chave in dados_teo:
    print(chave, "->", dados_teo[chave])


#%%

# de forma mais sofisticada
for chave, valor in dados_teo.items():
    print(chave, "->", valor)

# %%

dados_teo["estado civil"] = "solteiro"
dados_teo["fodase"] = None
# %%
dados_teo