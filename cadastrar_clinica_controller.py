# CONTROLLER de cadastro de clinica (MVC) - CRUD completo de Clinica.
# Pede dados a tela (ViewCadastrarClinica), cria/altera/remove objetos Clinica
# e os guarda no SistemaClinicas compartilhado.
from view_cadastrar_clinica import ViewCadastrarClinica
from clinica import Clinica


class CadastrarClinicaController:

    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_clinica = ViewCadastrarClinica()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def cadastrar(self, clinica_nome):
        # INCLUIR: o nome ja vem do fluxo de atendimento; pede o resto a tela,
        # cria a Clinica, guarda no sistema e devolve o objeto criado.
        nome = clinica_nome
        localizacao = self.__view_cadastrar_clinica.localizacao()
        descricao = self.__view_cadastrar_clinica.descricao()
        clinica = Clinica(nome=nome, localizacao=localizacao, descricao=descricao)
        self.add_sistema(clinica)
        return clinica

    def add_sistema(self, clinica):
        self.__sistema_clinicas.registrar_clinica(clinica)

    def listar(self):
        # LISTAR: monta as linhas de texto e manda a tela exibir
        # (controller prepara o dado, view so imprime).
        linhas = [f"{c.nome} | {c.localizacao} | {c.descricao}"
                  for c in self.__sistema_clinicas.clinicas]
        self.__view_cadastrar_clinica.listar_clinicas(linhas)

    def alterar(self):
        # ALTERAR: acha a clinica pelo nome, pede os novos dados e atualiza
        clinica = self.__buscar_clinica()
        if clinica is None:
            return
        dados = self.__view_cadastrar_clinica.pegar_dados_alteracao()
        clinica.localizacao = dados["localizacao"]
        clinica.descricao = dados["descricao"]
        self.__view_cadastrar_clinica.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: acha a clinica pelo nome e remove do sistema
        clinica = self.__buscar_clinica()
        if clinica is None:
            return
        self.__sistema_clinicas.remover_clinica(clinica)
        self.__view_cadastrar_clinica.sucesso_exclusao()

    def __buscar_clinica(self):
        # helper: pede o nome, procura na lista. Trata registro inexistente
        # (avisa pela tela e retorna None) - usado por alterar e excluir.
        nome = self.__view_cadastrar_clinica.pedir_nome()
        for clinica in self.__sistema_clinicas.clinicas:
            if clinica.nome == nome:
                return clinica
        self.__view_cadastrar_clinica.nao_encontrada()
        return None
