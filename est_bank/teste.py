from conta import ContaBancaria, Pix
from cliente import Cliente


def main():

    # Instâncias de cliente
    cliente1 = Cliente(
        nome="José da Silva",
        rg="000987-74",
        cpf="000.111.333-44",
        data_nascimento="02/02/02",
        agencia="000000-11",
        conta="963",
        saldo=3000
    )

    cliente2 = Cliente(
        nome="João Pereira",
        rg="000428-74",
        cpf="000.555.784-99",
        data_nascimento="05/07/05",
        agencia="000000-17",
        conta="791",
        saldo=5000
    )

    # Duas instâncias de ContaBancária
    conta1 = ContaBancaria(
        titular=cliente1.nome,
        agencia=cliente1.agencia,
        numero_conta=cliente1.conta,
        saldo=cliente1.saldo
    )

    conta2 = ContaBancaria(
        titular=cliente2.nome,
        agencia=cliente2.agencia,
        numero_conta=cliente2.conta,
        saldo=cliente2.saldo
    )

    print('\nEstado das contas 1 e 2 antes da transação via Pix')
    print(f'{conta1}\n{conta2}\n==============================================================\n')

    # Transação Pix
    pix = Pix()
    pix.enviar(origem=conta1, destino=conta2, valor=700)

    print('Estado das contas 1 e 2 após a transação via Pix')
    print(f'{conta1}\n{conta2}\n==============================================================')


if __name__ == '__main__':
    main()
