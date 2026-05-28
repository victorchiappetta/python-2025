# escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo
#%%

palavra = input("digite uma palavra:")
invertida = ''

# inverte a ordem da palavra utilizando [start:stop:step], onde step = -1 ==> faz com que a ordem seja invertida e comece do final 
invertida = palavra[::-1]

if invertida == palavra:
    print("palavra original =", palavra)
    print("palavra invertida =", invertida)
    print("portanto, é palíndromo")
else:
    print("palavra original =", palavra)
    print("palavra invertida =", invertida)
    print("portanto, não é palíndromo")

