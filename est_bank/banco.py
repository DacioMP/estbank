class Banco:
    banco_nome = 'EST Bank'
    banco_cnpj = '00.111.222/0001-33'

    def __str__(self):
        return f'Banco: {self.banco_nome}\nCNPJ: {self.banco_cnpj}'


def main():
    banco = Banco()
    print(banco)


if __name__ == '__main__':
    main()
