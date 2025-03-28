class ContaBancaria:
    def __init__(self, nome, cpf, numero_conta, agencia, banco):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.banco = banco
        self.saldo = 0.0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito deve ser positivo.')

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        else:
            print('Saque inválido. Verifique o valor e o saldo disponível.')

    def visualizar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

    def excluir_conta(self):
        del self
        print('Conta excluída com sucesso!')

# Exemplo de uso
if __name__ == "__main__":
    # Criando uma conta bancária
    conta = ContaBancaria(nome="João Silva", cpf="123.456.789-00", numero_conta="0001", agencia="1234", banco="Banco Exemplo")

    # Realizando operações
    conta.deposito(500)
    conta.visualizar_saldo()
    conta.saque(200)
    conta.visualizar_saldo()
    conta.excluir_conta()