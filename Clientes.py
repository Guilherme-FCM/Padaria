import abc

class Cliente(abc.ABC):
    def __init__(self, ID, nome, endereco, telefone):
        self.ID = ID
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

        @property
        def ID(self): 
            return self._ID

        @ID.setter
        def ID(self, valor):
            self._ID = valor

class PessoaFisica(Cliente):
    def __init__(self, ID, nome, endereco, telefone, CPF):
        super().__init__(ID, nome, endereco, telefone)
        self.CPF = CPF

class PessoaJuridica(Cliente):
    def __init__(self, ID, nome, endereco, telefone, CNPJ, NIE):
        super().__init__(ID, nome, endereco, telefone)
        self.CNPJ = CNPJ
        self.NIE = NIE

class Comprador(PessoaFisica):
    def __init__(self, ID, nome, endereco, telefone, CPF, dataCadastro):
        super().__init__(ID, nome, endereco, telefone, CPF)
        self.dataCadastro = dataCadastro

class Fornecedor(PessoaJuridica):
    def __init__(self, ID, nome, endereco, telefone, CNPJ, NIE, pessoaContato):
        super().__init__(ID, nome, endereco, telefone, CNPJ, NIE)
        self.pessoaContato = pessoaContato