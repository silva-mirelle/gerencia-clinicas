# MODEL (entidade). Tipo de atendimento (ex.: Consulta, Exame, Retorno).
# Entidade simples: so um nome.
class TipoAtendimento:
    def __init__(self, nome, codigo=None):
        # codigo e a chave de persistencia (artificial); atribuido pelo DAO
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor
