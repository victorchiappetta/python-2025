# %%
# lista = conjunto de elementos!
# listas não são arrays no python!!

# Uma maneira de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%

# lista pode ter vários tipos de elementos dentro dela e o exemplo abaixo mostra isso
teo = ["Téo", "Calvo", 32, True, "Casado", 2342.98]
print(teo)

# %%

#o tipo dela será... lista!
type(teo)

# %%

# lembrando que o índice da lista começa em 0 e vai até len-1

# idade
print(teo[2])

# renda
print(teo[5])

print(teo[0])

# %%

idades = [28, 42,43, 35,39, 28,38, 42, 34]

soma = sum(idades)
print("soma idades:", soma)

print("qtde idades:", len(idades))

print("media idades:", soma/len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

# %%

teo = [

       "Téo Calvo",
       32,
       True,
       "Casado",
       ["estagiario", "ds jr.", "ds pl", "ds sr.", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Claudia"]
      ]

print("Tamanho de téo:", len(teo))

print(teo[6][0])

exs = teo[6]
primeira_ex = exs[0]
print(primeira_ex)

# %%

tamanho = len(teo)
pos = tamanho - 1

exs = teo[pos] #lista das exs
teo[pos][len(exs) - 1] #acessa a última ex

# %%

teo[-1] #acessa o último elemento da lista
teo[-1][-1] #acessa a última ex desse elemento

# %%

# primeiros 4 elementos
teo[0:4] #intervalo é aberto

# %%

# acessa o 4º elemento e pega os dois últimos cargos preenchidos
teo[4][3:5]

# %%

# acessa o 4º elemento e pega os dois últimos cargos preenchidos
print(teo[4][3:])
print(teo[4][-2:]) #pega do elemento -2 até o final da lista

# %%

# primeiros 4 elementos
teo[:4]

# %%

# da onde começa e da onde termina
# se ocultar o 'start' vc começa do início da lista, do primeiro elemento
# se ocultar o 'stop' vc vai até o final da lista

# teo[ start : stop ]

print("start = oculto e stop = 3 ==>", teo[4][:3], "==> começa do 1º elemento e vai até o elemento 3(4º)")
print("start = 2 e stop = oculto ==>", teo[5][2:], "==> começa do elemento 2(3º) e vai até o final")


# %%

salarios = teo[5]

# teo[ start : stop : step ] ==> padrão o step é de 1 em 1

# se eu quiser inverter a ordem, faço o step = -1
salarios[::-1]

# se quiser ir de 2 em 2
salarios[::2]





