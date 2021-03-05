import abc

class Movimentacao(abc.ABC):
    def __init__(self, data, produto, quantidade):
        self.data = data
        self.produto = produto
        self.quantidade = quantidade

    @abc.abstractmethod   
    def valor(self): pass

class Compra(Movimentacao):
    def __init__(self, numeroNotaFiscal, data, produto, quantidade, valor, fornecedor):
        super().__init__(data, produto, quantidade)
        self.numeroNotaFiscal = numeroNotaFiscal
        self.valorPago = valor
        self.fornecedor = fornecedor

    def valor(self): return self.valorPago

class Venda(Movimentacao):
    def __init__(self, data, produto, quantidade, meioPagamento):
        super().__init__(data, produto, quantidade)
        self.meioPagamento = meioPagamento

    def valor(self): return self.produto.valorVenda() * self.quantidade