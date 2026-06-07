from view_registro_atendimento import ViewRegistroAtendimento
from cadastrar_clinica_controller import CadastrarClinicaController
from sistema_clinicas import SistemaClinicas
from cadastrar_paciente_controller import CadastrarPacienteController
#from view_cadastrar_profissional import CadastrarProfissionalController
from atendimento import Atendimento
from tipo_atendimento import TipoAtendimento


class RegistroAtendimentoController:

    def __init__(self):
        self.__view_registro_atendimento = ViewRegistroAtendimento()
        self.__sistema_clinicas = SistemaClinicas()
        self.__cadastrar_clinica_controller = CadastrarClinicaController(self.__sistema_clinicas)
        self.__cadastrar_paciente_controller = CadastrarPacienteController()
        #self.__atendimentos = []

    def iniciar_registro(self):
        clinica = self.valida_clinica()
        paciente = self.valida_paciente(clinica)
        dados = self.coletar_dados_atendimento()

        # BLOQUEIO: criar o Atendimento exige um ProfissionalSaude, que depende
        # do cadastro de profissional (responsabilidade da Mikaely).
        # Quando o modulo de profissional existir:
        #   profissional = self.valida_profissional(clinica)
        #   atendimento = Atendimento(clinica, paciente, profissional,
        #                             dados["data"], dados["horario_inicio"],
        #                             dados["horario_fim"], dados["tipo_atendimento"],
        #                             valor=0)
        self.__view_registro_atendimento.aguardando_profissional()

    def coletar_dados_atendimento(self):
        data = self.__view_registro_atendimento.data_atendimento()
        horario_inicio = self.__view_registro_atendimento.horario_inicio()
        horario_fim = self.__view_registro_atendimento.horario_fim()
        nome_tipo = self.__view_registro_atendimento.tipo_atendimento()
        tipo_atendimento = TipoAtendimento(nome_tipo)
        return {
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "tipo_atendimento": tipo_atendimento,
        }


    def valida_clinica(self):
        nome_clinica = self.__view_registro_atendimento.nome_clinica()
        for clinica in self.__sistema_clinicas.clinicas:
            if nome_clinica == clinica.nome:
                return clinica # Retorna objeto Clinica
        clinica = self.__cadastrar_clinica_controller.cadastrar(nome_clinica)
        return clinica # RETORNA OBJ CLINICA
    
    def valida_paciente(self, clinica):
        nome_paciente = self.__view_registro_atendimento.nome_paciente()
        for paciente in clinica.pacientes:
            if nome_paciente == paciente.nome:
                return paciente
        paciente = self.__cadastrar_paciente_controller.cadastrar(clinica, nome_paciente)
        return paciente