# CONTROLLER de relatorios (MVC).
# A CONTA fica no SistemaClinicas; aqui so pedimos o dado, formatamos as linhas
# e mandamos a ViewRelatorio exibir. (Por enquanto os 2 relatorios de procedimento.)
from view_relatorio import ViewRelatorio


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
