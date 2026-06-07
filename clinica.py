from paciente import Paciente

class Clinica:
    def __init__(self, nome, localizacao, descricao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__pacientes = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, valor):
        self.__localizacao = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def pacientes(self):
        return self.__pacientes
    
    @pacientes.setter
    def pacientes(self, paciente: Paciente):
        self.__pacientes.append(paciente)

    def remover_paciente(self, paciente):
        self.__pacientes.remove(paciente)