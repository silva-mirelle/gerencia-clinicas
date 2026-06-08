# MODEL (entidade) central. Um Atendimento liga clinica + paciente + profissional
# + tipo, com data/horario/valor. COMPOE procedimentos e AGREGA pagamentos.
class Atendimento:
    def __init__(self, clinica, paciente, profissional, data,
                 horario_inicio, horario_fim, tipo_atendimento, valor):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor
        self.__procedimentos = []  # procedimentos realizados neste atendimento
        self.__pagamentos = []     # pagamentos (suporta parcelamento)

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, valor):
        self.__clinica = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        self.__paciente = valor

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, valor):
        self.__profissional = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, valor):
        self.__horario_inicio = valor

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, valor):
        self.__horario_fim = valor

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, valor):
        self.__tipo_atendimento = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def procedimentos(self):
        return self.__procedimentos

    def adicionar_procedimento(self, procedimento):
        self.__procedimentos.append(procedimento)

    def remover_procedimento(self, procedimento):
        self.__procedimentos.remove(procedimento)

    @property
    def pagamentos(self):
        return self.__pagamentos

    def adicionar_pagamento(self, pagamento):
        self.__pagamentos.append(pagamento)

    def remover_pagamento(self, pagamento):
        self.__pagamentos.remove(pagamento)

    def calcular_valor_restante(self):
        # quanto ainda falta pagar = valor total - soma do que ja foi pago
        # (suporta pagamento parcial/parcelamento)
        total_pago = sum(p.valor_pago for p in self.__pagamentos)
        return self.__valor - total_pago
