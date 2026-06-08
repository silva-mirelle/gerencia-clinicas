# CONTROLLER de relatorios (MVC).
# A CONTA fica no SistemaClinicas; aqui so pedimos o dado, formatamos as linhas
# e mandamos a ViewRelatorio exibir. (Por enquanto os 2 relatorios de procedimento.)
from views.view_relatorio import ViewRelatorio


class RelatorioController:

    def __init__(self, sistema_clinicas):
        self.__view_relatorio = ViewRelatorio()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def procedimentos_mais_realizados(self):
        # pega (descricao, quantidade) ja ordenado e monta as linhas
        dados = self.__sistema_clinicas.procedimentos_mais_realizados()
        linhas = [f"{descricao}: {quantidade}x" for descricao, quantidade in dados]
        self.__view_relatorio.mostrar_relatorio("PROCEDIMENTOS MAIS REALIZADOS", linhas)

    def procedimentos_caros_baratos(self):
        # lista ordenada por custo -> primeiro = mais barato, ultimo = mais caro
        procedimentos = self.__sistema_clinicas.procedimentos_por_custo()
        if not procedimentos:
            self.__view_relatorio.mostrar_relatorio("PROCEDIMENTOS MAIS CAROS E MAIS BARATOS", [])
            return
        mais_barato = procedimentos[0]
        mais_caro = procedimentos[-1]
        linhas = [
            f"Mais caro:   {mais_caro.descricao} (R$ {mais_caro.custo})",
            f"Mais barato: {mais_barato.descricao} (R$ {mais_barato.custo})",
        ]
        self.__view_relatorio.mostrar_relatorio("PROCEDIMENTOS MAIS CAROS E MAIS BARATOS", linhas)

    def clinicas_mais_atendimentos(self):
        # (descricao, quantidade) ja ordenado por numero de atendimentos
        dados = self.__sistema_clinicas.clinicas_por_numero_atendimentos()
        linhas = [f"{nome}: {quantidade} atendimento(s)" for nome, quantidade in dados]
        self.__view_relatorio.mostrar_relatorio("CLINICAS COM MAIS ATENDIMENTOS", linhas)

    def atendimentos_caros_baratos(self):
        # lista ordenada por valor -> primeiro = mais barato, ultimo = mais caro
        atendimentos = self.__sistema_clinicas.atendimentos_por_valor()
        if not atendimentos:
            self.__view_relatorio.mostrar_relatorio("ATENDIMENTOS MAIS CAROS E MAIS BARATOS", [])
            return
        mais_barato = atendimentos[0]
        mais_caro = atendimentos[-1]
        linhas = [
            f"Mais caro:   {mais_caro.paciente.nome} em {mais_caro.clinica.nome} (R$ {mais_caro.valor})",
            f"Mais barato: {mais_barato.paciente.nome} em {mais_barato.clinica.nome} (R$ {mais_barato.valor})",
        ]
        self.__view_relatorio.mostrar_relatorio("ATENDIMENTOS MAIS CAROS E MAIS BARATOS", linhas)
