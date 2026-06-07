from view_iniciar import ViewIniciar
from registro_atendimento_controller import RegistroAtendimentoController
from sistema_clinicas import SistemaClinicas
from cadastrar_clinica_controller import CadastrarClinicaController
from cadastrar_paciente_controller import CadastrarPacienteController

class IniciarController:
    def __init__(self):
        self.__view_iniciar = ViewIniciar()
        self.__sistema_clinicas = SistemaClinicas()
        self.__cadastrar_clinica_controller = CadastrarClinicaController(self.__sistema_clinicas)
        self.__cadastrar_paciente_controller = CadastrarPacienteController(self.__sistema_clinicas)
        self.__registro_atendimento_controller = RegistroAtendimentoController(
            self.__sistema_clinicas,
            self.__cadastrar_clinica_controller,
            self.__cadastrar_paciente_controller,
        )

    def iniciar_atendimento(self):
        while True:
            escolha = self.__view_iniciar.menu()
            if escolha == '1':
                idade = self.__ler_idade()
                if self.valida_idade(idade):
                    self.__registro_atendimento_controller.iniciar_registro()
                else:
                    # menor de idade: barra e reinicia o menu
                    self.__view_iniciar.invalida_atendimento()
            elif escolha == '5':
                self.__cadastrar_clinica_controller.listar()
            elif escolha == '6':
                self.__cadastrar_paciente_controller.listar()
            elif escolha == '7':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __ler_idade(self):
        # repete ate o usuario digitar um numero inteiro valido
        while True:
            idade = self.__view_iniciar.idade_user()
            try:
                return int(idade)
            except ValueError:
                self.__view_iniciar.erro_idade_invalida()

    def valida_idade(self, idade: int):
        return idade > 18
    
    def registrar_atendimento(self):
        atendimento = Atendimento()
        return atendimento