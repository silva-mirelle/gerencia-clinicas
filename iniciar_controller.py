# CONTROLLER PRINCIPAL (MVC).
# E o "maestro" do sistema: dono do menu raiz, cria UM SistemaClinicas e o
# injeta em todos os controllers especificos (injecao de dependencia) para que
# todos compartilhem o mesmo "banco de dados" em memoria.
from view_iniciar import ViewIniciar
from registro_atendimento_controller import RegistroAtendimentoController
from sistema_clinicas import SistemaClinicas
from cadastrar_clinica_controller import CadastrarClinicaController
from cadastrar_paciente_controller import CadastrarPacienteController
from cadastrar_tipo_atendimento_controller import CadastrarTipoAtendimentoController
from cadastrar_profissional_controller import CadastrarProfissionalController
from registro_procedimento_controller import RegistroProcedimentoController
from relatorio_controller import RelatorioController
from registro_pagamento_controller import RegistroPagamentoController


class IniciarController:
    def __init__(self):
        self.__view_iniciar = ViewIniciar()
        # UM sistema unico compartilhado por todos os controllers (fonte de dados)
        self.__sistema_clinicas = SistemaClinicas()
        # controllers especificos recebem o mesmo sistema (injecao de dependencia)
        self.__cadastrar_clinica_controller = CadastrarClinicaController(self.__sistema_clinicas)
        self.__cadastrar_paciente_controller = CadastrarPacienteController(self.__sistema_clinicas)
        self.__cadastrar_tipo_atendimento_controller = CadastrarTipoAtendimentoController(self.__sistema_clinicas)
        self.__cadastrar_profissional_controller = CadastrarProfissionalController(self.__sistema_clinicas)
        self.__registro_procedimento_controller = RegistroProcedimentoController(self.__sistema_clinicas)
        self.__relatorio_controller = RelatorioController(self.__sistema_clinicas)
        self.__registro_pagamento_controller = RegistroPagamentoController(self.__sistema_clinicas)
        # o controller de registro recebe o sistema + os controllers ja prontos
        self.__registro_atendimento_controller = RegistroAtendimentoController(
            self.__sistema_clinicas,
            self.__cadastrar_clinica_controller,
            self.__cadastrar_paciente_controller,
        )

    def iniciar_atendimento(self):
        # laco do menu principal: pergunta a opcao a tela e roteia para a acao.
        # Cada opcao delega para um controller especifico (o maestro nao faz a regra).
        while True:
            escolha = self.__view_iniciar.menu()
            if escolha == '1':
                idade = self.__ler_idade()
                if self.valida_idade(idade):
                    self.__registro_atendimento_controller.iniciar_registro()
                else:
                    # menor de idade: barra e reinicia o menu
                    self.__view_iniciar.invalida_atendimento()
            elif escolha == '4':
                self.__cadastrar_profissional_controller.cadastrar()
            elif escolha == '5':
                self.__cadastrar_clinica_controller.listar()
            elif escolha == '6':
                self.__cadastrar_paciente_controller.listar()
            elif escolha == '7':
                self.__cadastrar_clinica_controller.alterar()
            elif escolha == '8':
                self.__cadastrar_clinica_controller.excluir()
            elif escolha == '9':
                self.__cadastrar_paciente_controller.alterar()
            elif escolha == '10':
                self.__cadastrar_paciente_controller.excluir()
            elif escolha == '11':
                self.__cadastrar_tipo_atendimento_controller.cadastrar()
            elif escolha == '12':
                self.__cadastrar_tipo_atendimento_controller.listar()
            elif escolha == '13':
                self.__cadastrar_tipo_atendimento_controller.alterar()
            elif escolha == '14':
                self.__cadastrar_tipo_atendimento_controller.excluir()
            elif escolha == '15':
                self.__cadastrar_profissional_controller.listar()
            elif escolha == '16':
                self.__cadastrar_profissional_controller.alterar()
            elif escolha == '17':
                self.__cadastrar_profissional_controller.excluir()
            elif escolha == '18':
                self.__registro_procedimento_controller.registrar()
            elif escolha == '19':
                self.__registro_procedimento_controller.listar()
            elif escolha == '20':
                self.__relatorio_controller.procedimentos_mais_realizados()
            elif escolha == '21':
                self.__relatorio_controller.procedimentos_caros_baratos()
            elif escolha == '22':
                self.__registro_pagamento_controller.registrar()
            elif escolha == '23':
                self.__registro_pagamento_controller.listar()
            elif escolha == '24':
                self.__registro_atendimento_controller.listar()
            elif escolha == '25':
                self.__registro_atendimento_controller.alterar()
            elif escolha == '26':
                self.__registro_atendimento_controller.excluir()
            elif escolha == '0':
                break  # sai do laco -> metodo retorna -> programa encerra
            else:
                self.__view_iniciar.opcao_invalida()

    def __ler_idade(self):
        # le a idade da tela e repete ate ser um inteiro valido.
        # try/except trata a entrada invalida (ex.: "abc" faria int() lancar ValueError).
        while True:
            idade = self.__view_iniciar.idade_user()
            try:
                return int(idade)
            except ValueError:
                self.__view_iniciar.erro_idade_invalida()

    def valida_idade(self, idade: int):
        # regra de negocio: so maior de 18 pode atendimento independente
        return idade > 18

    def registrar_atendimento(self):
        # TODO: codigo morto/placeholder - Atendimento exige 8 argumentos e nao
        # esta importado aqui. Mantido para implementacao futura; nao e chamado.
        atendimento = Atendimento()
        return atendimento
