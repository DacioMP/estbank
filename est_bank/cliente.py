from pessoa.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome, rg, cpf, data_nascimento, agencia, conta, saldo):
        super().__init__(nome, rg, cpf, data_nascimento)
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def __str__(self):
        return f"""
        Dados pessoais: 
        - Nome: {self._nome}
        - RG: {self._rg}
        - CPF: {self._cpf}
        - DT Nascimento: {self._data_nascimento}
        - Saldo: R${self._saldo}"""

    @property
    def titular(self):
        return self._nome

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo


def main():
    cliente = Cliente(
        nome="José da Silva",
        rg="000987-74",
        cpf="000.111.333-44",
        data_nascimento="02/02/02",
        agencia="4587",
        conta="963",
        saldo=3000
    )

    print(cliente)


if __name__ == '__main__':
    main()
