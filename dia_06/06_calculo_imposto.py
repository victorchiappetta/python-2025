# %%

# **kwargs é um dicionário
# **kwargs permite que adicione parametros nomeados de forma, tamanho, quantidade, etc. indefinidos dentro da função
def calc_imposto(preco:float, tx_base=0.03, **kwargs):
    imposto = preco * tx_base
    print("taxa base:", tx_base)

    for i in kwargs:
        print(i, ":", kwargs[i])
        imposto += preco * kwargs[i]
    
    return imposto

# %%

# preço e tx_base são obrigatórios e o resto é adicionado manualmente, com o uso de **kwargs
calc_imposto(100, 0.03, municipio=0.01, estadual=0.005, nacional=0.001)


#%%

# o exemplo acima pode ser mais enxuto utilizando um dicionário de impostos
impostos_gerais = {
    "municipio":0.01,
    "estadual":0.005,
    "nacional":0.001
}

# **impostos_gerais "estoura" o dicionário e cada par chave x valor é passado como argumento da função
# ou seja:
# municipio=0.01, estadual=0.005, nacional=0.001 == **impostos_gerais
calc_imposto(100, 0.03, **impostos_gerais)


# %%

# posso chamar mais impostos, como um internacional e isso não fere o escopo da função

calc_imposto(100, 0.03, **impostos_gerais, internacional=0.00005)
