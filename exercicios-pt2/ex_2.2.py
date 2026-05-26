#Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

#	O número x é impar
#           ou
#	O número x é par
#%%
numero = int(input("digite o número:"))

if numero % 2 == 0:
    print("o número ", numero, "é par!")
else:
    print("o número ", numero, "é ímpar!")