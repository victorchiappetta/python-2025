#%%
blabla = [17, 18, 19, 20]
print(blabla)

blabla.append(21) # .append() adiciona o valor 21 à lista blabla, alterando a lista original
print(blabla)


# %%
idades = []

# repete enquanto for verdadeiro
while True:
    idade = input("Entre com a idade: ")
    # se o usuário entrar com um valor em branco (der enter sem digitar nada) para o while
    if idade == "":
        break
    
    # adiciona cada elemento digitado à lista de idades
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)


print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)

