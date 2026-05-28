# escreva um prog que solicite frases. para parar de solicitar, ele pode apenas apertar 'enter'
# o programa deve apresentar cada frase e quantas vezes ela foi repetida
#%%

# dicionário armazena o par chave -> valor, onde chave == frase e valor == quantas vezes repetiu
frases = {}

while True:
    frase = input("digite uma frase:")
    
    # enter vazio finaliza o loop
    if frase == '':
        break

    # verifica se a 'frase' digitada está ou não dentro do dicionário frases
    # se não tem: acessa a chave 'frase' e atribui o valor de +1
    # se tem: acessa a chave 'frase' e atribui o valor dela mesma +1
    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1

# exibe cada par chave(== frase) -> valor( == quantas vezes repetiu)
for frase in frases:
    print(frase, "==>", frases[frase])

