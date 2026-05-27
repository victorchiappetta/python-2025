# %%

dados_teo = [32, 1, "Casado", "dev goLang"]
dados_teo

# %%

dados_teo.append("3241.43")
dados_teo[0] = 28
dados_teo

# %%

# tupla é uma lista imutável, desde que o elemento interno dela também seja
# 32, 1, "Casado", "dev golang são elementos imutáveis (int, string)!
# porém, a lista ["maria", "antonia"] é um elemento mutável e, portanto, pode sofrer alteração utilizando métodos como .append() por exemplo
tupla_teo = (32, 1, "Casado", "dev goLang", ["maria", "antonia"])

print(type(tupla_teo)) # tipo é tupla
print(tupla_teo)

# %%

# acessa o último elemento da tupla
tupla_teo[-1]

# como esse último elemento da tupla é uma lista (que é mutável), é possível adicionar "ana" a essa lista
tupla_teo[-1].append("ana")
print(tupla_teo)
