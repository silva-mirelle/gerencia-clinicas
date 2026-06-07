# MODEL (entidade). ProfissionalSaude E-UM Pessoa (heranca) + especialidade e
# registro profissional.
from pessoa import Pessoa


class ProfissionalSaude(Pessoa):
    def __init__(self, nome, celular, cpf, especialidade, registro_profissional):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, valor):
        self.__especialidade = valor

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, valor):
        self.__registro_profissional = valor

    def papel(self):
        return "Profissional de Saude"
