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