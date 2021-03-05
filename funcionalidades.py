from CompraVenda import Compra, Venda
from Clientes import Comprador, Fornecedor
from Produto import Produto

from datetime import date

# Variaveis Globais
fornecedores = []
clientes = []
produtos = []
compras = []
vendas = []

# Funcionalidades
def cadastrarCliente():
    print('\n-- Cadastro de Cliente --')

    id = len(clientes) + 1
    nome = input('Nome: ')
    endereco = input('Endereco: ')
    telefone = input('Telefone: ')
    cpf = input('CPF: ')

    # Cadastro
    clientes.append( Comprador(id, nome, endereco, telefone, cpf, date.today()) )

def cadastrarFornecedor():
    print('\n-- Cadastro de Fornecedor --')
    
    id = len(fornecedores) + 1
    nome = input('Nome: ')
    endereco = input('Endereco: ')
    telefone = input('Telefone: ')
    cnpj = input('CNPJ: ')
    nie = input('NIE: ')
    pessoaContato = input('Pessoa para contato: ')

    # Cadastro
    fornecedores.append( Fornecedor(id, nome, endereco, telefone, cnpj, nie, pessoaContato) )

def cadastrarProduto():
    print('\n-- Cadastro de Produto --')

    codigo = len(produtos) + 1
    descricao = input('Descricao: ')
    estoqueMinimo = int(input('Estoque mínimo: ') )
    estoque = int(input('Estoque: '))
    valorCusto = float(input('Valor de custo: '))
    percentualLucro = float(input('Percentual de lucro: '))

    # Cadastro
    produtos.append( Produto(codigo, descricao, estoqueMinimo, estoque, valorCusto, percentualLucro) )

def verProdutosCadastrados(): 
    print('\n-- Produtos Cadastrados --')
    print('Código  |  Descrição  |  Estoque/Minimo  |  Valor de Venda  |\n')

    for produto in produtos: 
        print(f'{ produto.codigo }  |  { produto.descricao }  |  { produto.estoque }/{ produto.estoqueMinimo }  |  { produto.valorVenda() }  |')
        

def registrarCompra(): 
    print('\n-- Registro de Compra --')

    data = input('Data: ')
    produto = input('Produto: ')
    quantidade = int(input('Quantidade: '))
    valor = float(input('Valor Pago: ') )
    numeroNotaFiscal = input('Número da nota fiscal: ')
    fornecedor = input('Fornecedor: ')    

    # Cadastro
    compras.append( Compra(numeroNotaFiscal, data, produto, quantidade, valor, fornecedor) )

def registrarVenda(): 
    print('\n-- Registro de Venda --')

    data = input('Data: ')
    produto = int(input('Código Produto: '))
    quantidade = int(input('Quantidade: '))
    meioPagamento = input('Meio de pagamento: ')   

    for p in produtos:
        if p.codigo == produto: 
            p.estoque -= quantidade
            produto = p 

    # Cadastro
    vendas.append( Venda(data, produto, quantidade, meioPagamento) )

def historico(): 
    totalCompras = totalVendas = 0

    print('\n-- Compras --')
    print('N° NF  |  Produto  |  Quantidade  |  Valor Total  |\n')

    for compra in compras:
        print(f'{ compra.numeroNotaFiscal }  |  { compra.produto }  |  { compra.quantidade }  |  { compra.valor() }  |')
        totalCompras += compra.valor()
    
    print('\n-- Vendas --')
    print('Data  |  Produto  |  Quantidade  |  Valor Total  |\n')

    for venda in vendas:
        print(f'{ venda.data }  |  { venda.produto.descricao }  |  { venda.quantidade }  |  { venda.valor() }  |')
        totalVendas += venda.valor()    

    print('\nValor Total de Compras:', totalCompras)
    print('Valor Total de Vendas:', totalVendas)