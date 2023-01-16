# Agregação


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome


class Conta:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente


# novo cliente
cli_novo = Cliente(nome="Fulano")

# nova conta, que agrega cliente
con_inter = Conta(cliente=cli_novo) 



# Herança
# herda tudo e mais o que ela oferecer


class ClientePF(Cliente):
    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome)
        self.cpf = cpf


class ClientePJ(Cliente):
    def __init__(self, nome: str, cnpj: str) -> None:
        super().__init__(nome)
        self.cnpj = cnpj


# Polimorfismo
# substitui a função de um metodo por cima




# Class Method

class Conta:
    _qtd = 0

    @classmethod
    def add_conta(cls):
        cls._qtd+=1

    @classmethod
    def quantidade_contas(cls):
        return cls._qtd

    def __init__(self) -> None:
        self.add_conta()
        ...



c_a = Conta()
c_b = Conta()
c_c = Conta()
c_d = Conta()


print(Conta.quantidade_contas())