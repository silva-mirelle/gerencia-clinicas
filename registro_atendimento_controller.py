# CONTROLLER de registro de atendimento (MVC).
# Orquestra o fluxo de marcar um atendimento: valida/cadastra clinica e paciente,
# coleta os dados, e (futuramente) cria o objeto Atendimento.
from view_registro_atendimento import ViewRegistroAtendimento
#from view_cadastrar_profissional import CadastrarProfissionalController
from atendimento import Atendimento
from tipo_atendimento import TipoAtendimento


class RegistroAtendimentoController:

    # Recebe (injecao de dependencia) o sistema compartilhado e os controllers de
    # cadastro ja prontos, para reaproveitar clinica/paciente ja existentes.
    def __init__(self, sistema_clinicas, cadastrar_clinica_controller, cadastrar_paciente_controller):
        self.__view_registro_atendimento = ViewRegistroAtendimento()
        self.__sistema_clinicas = sistema_clinicas
        self.__cadastrar_clinica_controller = cadastrar_clinica_controller
        self.__cadastrar_paciente_controller = cadastrar_paciente_controller
        #self.__atendimentos = []

    def iniciar_registro(self):
        # passo a passo do atendimento: clinica -> paciente -> dados
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
        # coleta os campos proprios do atendimento via tela e devolve um dict pronto
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
        # busca a clinica pelo nome digitado; se nao existir, cadastra na hora.
        # Sempre retorna o OBJETO Clinica (nao True), pois o atendimento precisa dele.
        nome_clinica = self.__view_registro_atendimento.nome_clinica()
        for clinica in self.__sistema_clinicas.clinicas:
            if nome_clinica == clinica.nome:
                return clinica  # clinica ja existia (caminho feliz)
        clinica = self.__cadastrar_clinica_controller.cadastrar(nome_clinica)
        return clinica  # nao existia -> foi cadastrada (caminho triste)

    def valida_paciente(self, clinica):
        # mesmo padrao da clinica: acha o paciente DENTRO da clinica ou cadastra.
        # Retorna o OBJETO Paciente.
        nome_paciente = self.__view_registro_atendimento.nome_paciente()
        for paciente in clinica.pacientes:
            if nome_paciente == paciente.nome:
                return paciente
        paciente = self.__cadastrar_paciente_controller.cadastrar(clinica, nome_paciente)
        return paciente
