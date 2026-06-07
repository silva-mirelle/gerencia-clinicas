from view_registro_atendimento import ViewRegistroAtendimento
from cadastrar_clinica_controller import CadastrarClinicaController
from sistema_clinicas import SistemaClinicas
#from view_cadastrar_paciente import CadastrarPacienteController
#from view_cadastrar_profissional import CadastrarProfissionalController
from atendimento import Atendimento


class RegistroAtendimentoController:

    def __init__(self):
        self.__view_registro_atendimento = ViewRegistroAtendimento()
        self.__sistema_clinicas = SistemaClinicas()
        self.__cadastrar_clinica_controller = CadastrarClinicaController(self.__sistema_clinicas)
        #self.__atendimentos = []

    def iniciar_registro(self):
        clinica_valida = self.valida_clinica()
        if clinica_valida:
            # escopo atual termina aqui — validar paciente entra no próximo commit
            pass

    def valida_clinica(self):
        clinica = self.__view_registro_atendimento.nome_clinica()
        for c in self.__sistema_clinicas.clinicas:
            if clinica == c.nome:
                return True
        self.__cadastrar_clinica_controller.cadastrar(clinica)
        return True