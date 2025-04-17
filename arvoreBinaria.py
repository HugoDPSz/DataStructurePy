class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def inserir(no, valor):
    if no is None:
        return No(valor)
    if valor < no.valor:
        no.esq = inserir(no.esq, valor)
    else:
        no.dir = inserir(no.dir, valor)
    return no
    
def buscar(no, valor):
    if no is None or no.valor == valor:
        return no
    if valor < no.valor:
        return buscar(no.esq, valor)
    return buscar(no.dir)

def remover(no, valor):
    if no is None:
        return no
    if valor < no.valor:
        no.esq = remover(no.esq, valor)
    elif valor > no.valor:
        no.dir = remover(no.dir, valor)
    else:
        if no.esq is None:
            return no.dir
        if no.dir is None:
            return no.esq
        temp = valor_min(no.dir)
        no.valor = temp.valor
        no.dir = remover(no.dir, temp.valor)
    return no

def valor_min(no):
    atual = no
    while atual.esq is not None:
        atual = atual.esq
    return atual