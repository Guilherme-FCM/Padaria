class Produto:
    def __init__(self, codigo, descricao, estoqueMinimo, estoque, valorCusto, percentualLucro):
        self.codigo = codigo
        self.descricao = descricao
        self.estoqueMinimo = estoqueMinimo
        self.estoque = estoque
        self.valorCusto = valorCusto
        self.percentualLucro = percentualLucro

        @property
        def codigo(self): 
            return self._codigo

        @codigo.setter
        def codigo(self, valor):
            self._codigo = valor

    def valorVenda(self): return self.valorCusto + ( self.valorCusto * self.percentualLucro / 100 ) 