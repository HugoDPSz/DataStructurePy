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

    def _buscar_no(self, no, codigo):
        if no is None or no.codigo == codigo:
            return no
        if codigo < no.codigo:
            return self._buscar_no(no.esq, codigo)
        else:
            return self._buscar_no(no.dir, codigo)
        
    def remover(self, codigo):
        if self._buscar_no(self.raiz, codigo) is None:
            return
        self.raiz = self._remover_no(self.raiz, codigo)
        if self.raiz is not None:
            self.raiz.cor = 'preto'
        
    def _remover_no(self, no, codigo):
        if codigo < no.codigo:
            if not self._is_red(no.esq) and not self._is_red(no.esq.esq):
                no = self._mover_para_esquerda(no)
            no.esq = self._remover_no(no.esq, codigo)
        else:
            if self._is_red(no.esq):
                no = self._rotacionar_direita(no)
            if codigo == no.codigo and no.dir is None:
                return None
            if not self._is_red(no.dir) and not self._is_red(no.dir.esq):
                no = self._mover_para_direita(no)
            if codigo == no.codigo:
                x = self._minimo(no.dir)
                no.codigo = x.codigo
                no.nome = x.nome
                no.status = x.status
                no.dir = self._remover_min(no.dir)
            else:
                no.dir = self._remover_no(no.dir, codigo)
        return self._balancear(no)
    
    def _mover_para_esquerda(self, no):
        self._trocar_cores(no)
        if self._is_red(no.dir.esq):
            no.dir = self._rotacionar_direita(no.dir)
            no = self._rotacionar_esquerda(no)
            self._trocar_cores(no)
        return no
    
    def _mover_para_direita(self, no):
        self._trocar_cores(no)
        if self._is_red(no.esq.esq):
            no = self._rotacionar_direita(no)
            self._trocar_cores(no)
        return no
    
    def _remover_min(self, no):
        if no.esq is None:
            return None
        if not self._is_red(no.esq) and not self._is_red(no.esq.esq):
            no = self._mover_para_esquerda(no)
        no.esq = self._remover_min(no.esq)
        return self._balancear(no)
    
    def _balancear(self, no):
        if self._is_red(no.dir):
            no = self._rotacionar_esquerda(no)
        if self._is_red(no.esq) and self._is_red(no.esq.esq):
            no = self._rotacionar_direita(no)
        if self._is_red(no.esq) and self._is_red(no.dir):
            self._trocar_cores(no)
        return no
    
    def _minimo(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual