# %%
#tabuada usando while

numero = int(input("entre com o numero:"))
count = 1

while count <= 10:
    print(numero, "X", count, "=", numero * count)
    count += 1  #==> count = count + 1


print("Acabou!!")

#%%

#tabuada usando for

numero = int(input("entre com com o numero:"))

for i in range(1,11):
    print(numero, "X", i, "=", numero * i)

print("Acabou também!")