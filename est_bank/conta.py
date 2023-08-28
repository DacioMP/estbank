from banco import Banco
from datetime import datetime
import time


class ContaBancaria(Banco):

    def __init__(self, titular, agencia, numero_conta, saldo):
        self._titular = titular
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    def __str__(self):
        return f'Conta bancária: {self._agencia}/{self._numero_conta} - {self._titular} - R${self._saldo:.2f}'

    @property
    def titular(self):
        return self._titular

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValueError("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            raise ValueError("O valor do saque deve ser maior que zero e menor ou igual ao saldo da conta.")


class Pix:

    @staticmethod
    def enviar(origem, destino, valor):
        print(f'Enviando pix de R${valor}...')
        time.sleep(3)
        if 0 < valor <= origem.saldo:
            origem.sacar(valor)
            destino.depositar(valor)

            agora = datetime.now()
            d = agora.strftime("%d/%m/%Y, %H:%M:%S")

            print(f"Transação Pix de R${valor:.2f} realizada com sucesso.\n")
            print("COMPROVANTE")
            print(f"ENVIADO PARA: {destino.titular}\nINSTITUIÇÃO: {destino.banco_nome}\nQUANTIA: R${valor}\nDATA: {d}\n")
            time.sleep(2)
        else:
            print("Saldo insuficiente ou valor inválido para transação Pix.\n")
            time.sleep(2)


def main():
    conta1 = ContaBancaria(
        titular="José da Silva",
        agencia="000000-11",
        numero_conta="456",
        saldo=1200
    )

    print(conta1)


if __name__ == '__main__':
    main()
