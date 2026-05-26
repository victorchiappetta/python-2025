#Faça um programa que receba o nome e a idade de uma pessoa. 

#Caso essa pessoa tenha menos de 18 anos, exiba o aviso:
#	“Fulano, você não pode dirigir nem beber”

#Para as pessoas entre 18 e 65 anos, exiba o aviso:
#	“Fulano, bebida liberada! Só não vale dirigir!”

#Para as pessoas com mais de 65 anos, exiba o aviso:
#	“Fulano, beba com muita moderação!”

#%%
nome = input("digite seu nome:")
idade = int(input("digite a sua idade:"))

if idade>=18 and idade<=65:
    print("sua idade eh:", idade)
    print(nome, ", bebida liberada! Só não vale dirigir!")

elif idade>65:
    print("sua idade eh:", idade)
    print(nome, ", beba com muita moderação!")

else:
    print("sua idade eh:", idade)
    print(nome, ", você não pode dirigir nem beber!")