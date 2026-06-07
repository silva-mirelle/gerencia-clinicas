#from clinica_controlador import Clinica
#from atendimento import Atendimento
from tela_atendimento import TelaAtendimento

class AtendimentoController:
    def __init__(self):
        self.__tela_atendimento = TelaAtendimento()
        #self.__atendimentos = []

    def iniciar_atendimento(self):
        while True:
            escolha = self.__tela_atendimento.menu()
            if escolha == '1':
                # VALIDA IDADE DO PACIENTE 
                idade = self.__tela_atendimento.idade_user()
                
                # SEGUE COM ATENDIMENTO IF TRUE - IMPLEMENTAR NO PROX COMMIT
                if self.valida_idade(idade):
                    #self.__tela_atendimento.registrar_atendimento()
                    break 
                else: 
                    # INVALIDA ATENDIMENTO E REINICIA MENU
                    self.__tela_atendimento.invalida_atendimento()
            if escolha=='5':
                break 
         
    def valida_idade(self, idade: int):
        return True if int(idade)>18 else False
    
    def registrar_atendimento(self):
        print("REGISTREI")