# CONTROLLER de cadastro de tipo de atendimento (MVC) - CRUD completo.
# TipoAtendimento e simples (so um nome); fica numa lista global no SistemaClinicas.
from view_cadastrar_tipo_atendimento import ViewCadastrarTipoAtendimento
from tipo_atendimento import TipoAtendimento
from validacao import ler_obrigatorio


class CadastrarTipoAtendimentoController:

    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_tipo = ViewCadastrarTipoAtendimento()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def cadastrar(self):
        # INCLUIR: pede o nome, cria o tipo, guarda no sistema e devolve o objeto
        nome = ler_obrigatorio(self.__view_cadastrar_tipo.pegar_nome,
                               self.__view_cadastrar_tipo.erro_campo_obrigatorio)
        tipo = TipoAtendimento(nome)
        self.__sistema_clinicas.registrar_tipo_atendimento(tipo)
        return tipo

    def listar(self):
        # LISTAR: nomes dos tipos cadastrados
        linhas = [tipo.nome for tipo in self.__sistema_clinicas.tipos_atendimento]
        self.__view_cadastrar_tipo.listar_tipos(linhas)

    def alterar(self):
        # ALTERAR: acha pelo nome e troca o nome
        tipo = self.__buscar_tipo()
        if tipo is None:
            return
        tipo.nome = self.__view_cadastrar_tipo.novo_nome()
        self.__view_cadastrar_tipo.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: acha pelo nome e remove do sistema
        tipo = self.__buscar_tipo()
        if tipo is None:
            return
        self.__sistema_clinicas.remover_tipo_atendimento(tipo)
        self.__view_cadastrar_tipo.sucesso_exclusao()

    def __buscar_tipo(self):
        # helper: pede o nome e procura; trata nao encontrado (avisa e retorna None)
        nome = self.__view_cadastrar_tipo.pedir_nome()
        for tipo in self.__sistema_clinicas.tipos_atendimento:
            if tipo.nome == nome:
                return tipo
        self.__view_cadastrar_tipo.nao_encontrado()
        return None
