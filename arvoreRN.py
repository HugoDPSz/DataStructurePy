class No:
    def __init__(self, codigo, nome, status):
        self.codigo = codigo
        self.nome = nome
        self.status = status
        self.esq = None
        self.dir = None
        self.cor = 'vermelho'

class ArvoreRubroNegra:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, nome, status):
        self.raiz = self._inserir_no(self.raiz, codigo, nome, status)
        #Define raiz como preta
        self.raiz.cor = 'preto'

    def _inserir_no(self, no, codigo, nome, status):
        if no is None:
            #Cria um novo no se o no for nulo
            return No(codigo, nome, status)
        if codigo < no.codigo:
            #Insere a esquerda
            no.esq = self._inserir_no(no.esq, codigo, nome, status)
        else:
            #Insere a direita
            no.dir = self._inserir_no(no.dir, codigo, nome, status)

        #Balancear
        if self._is_red(no.dir) and not self._is_red(no.esq):
            no = self._rotacionar_esquerda(no)
        if self._is_red(no.esq) and self._is_red(no.esq.esq):
            no = self._rotacionar_direita(no)
        if self._is_red(no.esq) and self._is_red(no.dir):
            self._trocar_cores(no)

        return no
    
    def _is_red(self, no):
        #Verificar se o no e vermelho
        return no is not None and no.cor == 'vermelho'
    
    def _rotacionar_esquerda(self, no):
        x = no.dir
        no.dir = x.esq
        x.esq = no
        x.cor = no.cor
        no.cor = 'vermelho'
        return x
    
    def _rotacionar_direita(self, no):
        x = no.esq
        no.esq = x.dir
        x.dir = no
        x.cor = no.cor
        no.cor = 'vermelho'
        return x
    
    def _trocar_cores(self, no):
        no.cor = 'vermelho'
        no.esq.cor = 'preto'
        no.dir.cor = 'preto'

    def buscar(self, codigo):
        return self._buscar_no(self.raiz, codigo)
    
    