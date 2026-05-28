#%%

# *args => absorve tudo que é não obrigatório na função, vem sempre no final dos argumentos obrigatórios
# *args é uma tupla ou lista de N elementos

def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    # (len(args)+2) significa que se não tiver outros elementos além de a e b, ou seja, args == 0, a média é calculada corretamente
    # quer dizer => args == 0, media = soma (a, b, 0) / (len(0)+2) == soma (a,b) / (0 + 2) == soma(a,b)/2. Dessa forma, a fórmula permanece correta.
    return soma(a, b, *args) / (len(args)+2)

a = float(input("entre com o valor de a: "))
b = float(input("entre com o valor de b: "))
c = float(input("entre com o valor de c: "))
d = float(input("entre com o valor de d: "))
e = float(input("entre com o valor de e: "))

print("Média:", media(a,b,c,d,e))


