# MODEL (entidade). Paciente E-UM Pessoa (heranca) + data de nascimento.
from models.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf, data_nascimento):
        super().__init__(nome, celular, cpf)  # reaproveita nome/celular/cpf da Pessoa
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self.__data_nascimento = valor

    def papel(self):
        return "Paciente"
