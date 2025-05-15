lista = [40, 20, 50, 30, 10]
for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave

print(lista)