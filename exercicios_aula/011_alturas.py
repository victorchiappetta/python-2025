# faça um programa que receba 4 alturas usando um laço de repetição e realiza a soma das alturas
#%%
soma = 0
quantidade_entradas = 4

for i in range(quantidade_entradas):
    alturas = input("entre com as alturas")
    alturas = float(alturas)
    soma = soma + alturas

print(soma)