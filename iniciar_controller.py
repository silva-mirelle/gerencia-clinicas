from view_iniciar import ViewIniciar
from registro_atendimento_controller import RegistroAtendimentoController

class IniciarController:
    def __init__(self):
        self.__view_iniciar = ViewIniciar()
        self.__registro_atendimento_controller = RegistroAtendimentoController()

    def iniciar_atendimento(self):
        while True:
            escolha = self.__view_iniciar.menu()
            if escolha == '1':
                # VALIDA IDADE DO PACIENTE 
                idade = self.__view_iniciar.idade_user()
    
                # SEGUE COM ATENDIMENTO IF TRUE - IMPLEMENTAR NO PROX COMMIT
                if self.valida_idade(idade):
                    self.__registro_atendimento_controller.iniciar_registro()
                    break 
                else: 
                    # INVALIDA ATENDIMENTO E REINICIA MENU
                    self.__view_iniciar.invalida_atendimento()
            if escolha=='5':
                break 
         
    def valida_idade(self, idade: int):
        return True if int(idade)>18 else False
    
    def registrar_atendimento(self):
        atendimento = Atendimento()
        return atendimento