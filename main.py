from Interface import Interface
from funcionalidades import *

interface = Interface({
    'Cadastrar Cliente':    cadastrarCliente,
    'Cadastrar Fornecedor': cadastrarFornecedor,
    'Cadastrar Produto':    cadastrarProduto,
    'Produtos Cadastrados': verProdutosCadastrados,
    'Registrar Compra':     registrarCompra,
    'Registrar Venda':      registrarVenda,
    'Histórico':            historico
}, 'Padaria do Sr. Joaquim').start()