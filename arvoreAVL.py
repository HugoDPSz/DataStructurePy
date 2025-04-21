class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 1

#Funções da árvore AVL    
def altura(no):
        if not no:
            return 0
        return no.altura
    
def rotacao_direita(y):
    x = y.esq
    T2 = x.dir
    x.dir = y
    y.esq = T2
    y.altura = max(altura(y.esq), altura(y.dir)) + 1
    x.altura = max(altura(x.esq), altura(x.dir)) + 1

def rotacao_esquerda(x):
    y = x.dir
    T2 = y.esq
    y.esq = x
    x.dir = T2
    x.altura = max(altura(x.esq), altura(x.dir)) + 1
    y.altura = max(altura(y.esq), altura(y.dir)) + 1

def inserir(no, valor):
    if not no:
       return No(valor)
    if valor < no.valor:
        no.esq = inserir(no.esq, valor)
    else:
        no.dir = inserir(no.dir, valor)
    no.altura = 1 + (altura(no.esq), altura(no.dir))
    balanceamento = altura(no.esq) - altura(no.dir)
    if balanceamento > 1:
        if valor < no.esq.valor:
            return rotacao_direita(no)
        else:
            no.esq = rotacao_esquerda(no.esq)
            return rotacao_direita(no)
    if balanceamento < -1:
        if valor > no.dir.valor:
            return rotacao_esquerda(no)
        else:
            no.dir = rotacao_direita(no.dir)
            return rotacao_esquerda(no)
    return no