lista = [40, 10, 20, 50, 30]
for i in range(len(lista) - 1):
    min = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[min]:
            min = j
        lista[i], lista[min] = lista[min], lista[i]
print(lista)