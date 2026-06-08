# CONTROLLER de registro de pagamento (MVC).
# Pagamentos sao registrados DENTRO de um atendimento. Suporta 3 modalidades
# (Dinheiro/PIX/Cartao) e PARCELAMENTO: cada pagamento parcial soma, e o
# calcular_valor_restante (no model Atendimento) mostra quanto ainda falta.
from view_registro_pagamento import ViewRegistroPagamento
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_pix import PagamentoPix
from pagamento_cartao import PagamentoCartao


class RegistroPagamentoController:

    def __init__(self, sistema_clinicas):
        self.__view_registro_pagamento = ViewRegistroPagamento()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def registrar(self):
        # INCLUIR: escolhe o atendimento, coleta data/valor + dados da modalidade,
        # cria o Pagamento certo (polimorfismo) e adiciona ao atendimento.
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        data = self.__view_registro_pagamento.data_pagamento()
        valor = self.__ler_valor()
        pagamento = self.__criar_pagamento(atendimento, data, valor)
        if pagamento is None:
            return  # modalidade invalida
        atendimento.adicionar_pagamento(pagamento)
        # parcelamento: mostra quanto ainda falta pagar do atendimento
        restante = atendimento.calcular_valor_restante()
        self.__view_registro_pagamento.sucesso(restante)

    def __criar_pagamento(self, atendimento, data, valor):
        # cada modalidade instancia uma SUBCLASSE diferente de Pagamento (heranca).
        # o paciente do pagamento e o proprio paciente do atendimento.
        modalidade = self.__view_registro_pagamento.escolher_modalidade()
        paciente = atendimento.paciente
        if modalidade == '1':
            return PagamentoDinheiro(data, atendimento, paciente, valor)
        if modalidade == '2':
            cpf_pagador = self.__view_registro_pagamento.cpf_pagador()
            return PagamentoPix(data, atendimento, paciente, valor, cpf_pagador)
        if modalidade == '3':
            numero_cartao = self.__view_registro_pagamento.numero_cartao()
            bandeira = self.__view_registro_pagamento.bandeira()
            return PagamentoCartao(data, atendimento, paciente, valor, numero_cartao, bandeira)
        self.__view_registro_pagamento.modalidade_invalida()
        return None

    def listar(self):
        # LISTAR: percorre os pagamentos de todos os atendimentos.
        # forma() e polimorfico (cada subclasse devolve "Dinheiro"/"PIX"/"Cartao").
        linhas = []
        for atendimento in self.__sistema_clinicas.atendimentos:
            for pagamento in atendimento.pagamentos:
                linhas.append(
                    f"{pagamento.forma()} | R$ {pagamento.valor_pago} "
                    f"| data: {pagamento.data} | paciente: {atendimento.paciente.nome}"
                )
        self.__view_registro_pagamento.listar_pagamentos(linhas)

    def __selecionar_atendimento(self):
        # mesma selecao numerada do registro de procedimento; mostra valor e restante
        atendimentos = self.__sistema_clinicas.atendimentos
        if not atendimentos:
            self.__view_registro_pagamento.sem_atendimentos()
            return None
        linhas = [
            f"{a.paciente.nome} | {a.clinica.nome} | {a.data} "
            f"| valor: {a.valor} | restante: {a.calcular_valor_restante()}"
            for a in atendimentos
        ]
        escolha = self.__view_registro_pagamento.selecionar_atendimento(linhas)
        if not escolha.isdigit():
            self.__view_registro_pagamento.selecao_invalida()
            return None
        indice = int(escolha) - 1
        if indice < 0 or indice >= len(atendimentos):
            self.__view_registro_pagamento.selecao_invalida()
            return None
        return atendimentos[indice]

    def __ler_valor(self):
        # le o valor pago e converte pra float; repete se nao for numero
        while True:
            try:
                return float(self.__view_registro_pagamento.valor_pago())
            except ValueError:
                self.__view_registro_pagamento.erro_valor_invalido()

    def alterar(self):
        # ALTERAR: escolhe atendimento -> escolhe pagamento -> troca data e valor.
        # (campos da modalidade, ex.: cpf/cartao, ficam fixos pra simplificar.)
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        pagamento = self.__selecionar_pagamento(atendimento)
        if pagamento is None:
            return
        pagamento.data = self.__view_registro_pagamento.data_pagamento()
        pagamento.valor_pago = self.__ler_valor()
        self.__view_registro_pagamento.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: escolhe atendimento -> escolhe pagamento -> remove do atendimento
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        pagamento = self.__selecionar_pagamento(atendimento)
        if pagamento is None:
            return
        atendimento.remover_pagamento(pagamento)
        self.__view_registro_pagamento.sucesso_exclusao()

    def __selecionar_pagamento(self, atendimento):
        # selecao numerada dos pagamentos DAQUELE atendimento; objeto ou None
        pagamentos = atendimento.pagamentos
        if not pagamentos:
            self.__view_registro_pagamento.sem_pagamentos()
            return None
        linhas = [f"{p.forma()} | R$ {p.valor_pago} | data: {p.data}" for p in pagamentos]
        escolha = self.__view_registro_pagamento.selecionar_pagamento(linhas)
        if not escolha.isdigit():
            self.__view_registro_pagamento.selecao_invalida()
            return None
        indice = int(escolha) - 1
        if indice < 0 or indice >= len(pagamentos):
            self.__view_registro_pagamento.selecao_invalida()
            return None
        return pagamentos[indice]
