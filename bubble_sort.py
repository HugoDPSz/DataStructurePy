def bubble_sort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]