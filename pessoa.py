from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, celular, cpf):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, valor):
        self.__celular = valor

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    @abstractmethod
    def papel(self):
        pass
