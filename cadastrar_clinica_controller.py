from view_cadastrar_clinica import ViewCadastrarClinica
from clinica import Clinica

class CadastrarClinicaController:

    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_clinica = ViewCadastrarClinica()
        self.__sistema_clinicas = sistema_clinicas
    
    def cadastrar(self, clinica_nome):
        nome = clinica_nome
        localizacao = self.__view_cadastrar_clinica.localizacao()
        descricao = self.__view_cadastrar_clinica.descricao()
        clinica = Clinica(nome=nome, localizacao=localizacao, descricao=descricao)
        self.add_sistema(clinica)
        return clinica
    
    def add_sistema(self, clinica):
        self.__sistema_clinicas.registrar_clinica(clinica)

    def listar(self):
        linhas = [f"{c.nome} | {c.localizacao} | {c.descricao}"
                  for c in self.__sistema_clinicas.clinicas]
        self.__view_cadastrar_clinica.listar_clinicas(linhas)

    def alterar(self):
        clinica = self.__buscar_clinica()
        if clinica is None:
            return
        dados = self.__view_cadastrar_clinica.pegar_dados_alteracao()
        clinica.localizacao = dados["localizacao"]
        clinica.descricao = dados["descricao"]
        self.__view_cadastrar_clinica.sucesso_alteracao()

    def excluir(self):
        clinica = self.__buscar_clinica()
        if clinica is None:
            return
        self.__sistema_clinicas.remover_clinica(clinica)
        self.__view_cadastrar_clinica.sucesso_exclusao()

    def __buscar_clinica(self):
        nome = self.__view_cadastrar_clinica.pedir_nome()
        for clinica in self.__sistema_clinicas.clinicas:
            if clinica.nome == nome:
                return clinica
        self.__view_cadastrar_clinica.nao_encontrada()
        return None