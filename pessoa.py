# MODEL (entidade) abstrata. Base comum de Paciente e ProfissionalSaude.
# E abstrata (ABC) + tem metodo abstrato papel(), entao Pessoa NAO pode ser
# instanciada diretamente: cada subclasse e obrigada a implementar papel().
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
        # cada subclasse devolve seu papel (ex.: "Paciente") - polimorfismo
        pass
