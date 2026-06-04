class Procedimento:
    def __init__(self, descricao, custo, profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, valor):
        self.__custo = valor

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, valor):
        self.__profissional = valor
