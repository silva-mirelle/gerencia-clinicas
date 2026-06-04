from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, data, atendimento, paciente, valor_pago):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, valor):
        self.__atendimento = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        self.__paciente = valor

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor):
        self.__valor_pago = valor

    @abstractmethod
    def forma(self):
        pass
