# MODEL. Pagamento via cartao de credito - E-UM Pagamento (heranca) + numero do
# cartao e bandeira.
from models.pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def __init__(self, data, atendimento, paciente, valor_pago, numero_cartao, bandeira):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, valor):
        self.__numero_cartao = valor

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, valor):
        self.__bandeira = valor

    def forma(self):
        return "Cartao de Credito"
