class Pessoa:
    def __init__(self, nome, rg, cpf, data_nascimento):
        self._nome = nome
        self._rg = rg
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"Dados pessoais\n Nome: {self._nome}\n RG: {self._rg}\n CPF: {self._cpf}\n DT Nascimento: {self._data_nascimento}"

    @property
    def nome(self):
        return self._nome

    @property
    def rg(self):
        return self._rg

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento


def main():
    pessoa = Pessoa(
        nome="João da Silva",
        rg="000000-11",
        cpf="000.000.000-00",
        data_nascimento="02/02/02",
    )

    print(pessoa)


if __name__ == '__main__':
    main()
