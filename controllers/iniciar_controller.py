# CONTROLLER PRINCIPAL (MVC).
# E o "maestro" do sistema: dono do menu raiz, cria UM SistemaClinicas e o
# injeta em todos os controllers especificos (injecao de dependencia) para que
# todos compartilhem o mesmo "banco de dados" em memoria.
# O menu e em 2 niveis: menu principal (por area) -> submenu (acoes da area).
from views.view_iniciar import ViewIniciar
from controllers.registro_atendimento_controller import RegistroAtendimentoController
from models.sistema_clinicas import SistemaClinicas
from controllers.cadastrar_clinica_controller import CadastrarClinicaController
from controllers.cadastrar_paciente_controller import CadastrarPacienteController
from controllers.cadastrar_tipo_atendimento_controller import CadastrarTipoAtendimentoController
from controllers.cadastrar_profissional_controller import CadastrarProfissionalController
from controllers.registro_procedimento_controller import RegistroProcedimentoController
from controllers.relatorio_controller import RelatorioController
from controllers.registro_pagamento_controller import RegistroPagamentoController


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
        self.__registro_atendimento_controller = RegistroAtendimentoController(
            self.__sistema_clinicas,
            self.__cadastrar_clinica_controller,
            self.__cadastrar_paciente_controller,
        )

    def iniciar_atendimento(self):
        # MENU PRINCIPAL: cada opcao abre o submenu de uma area.
        while True:
            escolha = self.__view_iniciar.menu()
            if escolha == '1':
                self.__menu_atendimento()
            elif escolha == '2':
                self.__menu_clinicas()
            elif escolha == '3':
                self.__menu_pacientes()
            elif escolha == '4':
                self.__menu_profissionais()
            elif escolha == '5':
                self.__menu_tipos()
            elif escolha == '6':
                self.__menu_procedimentos()
            elif escolha == '7':
                self.__menu_pagamentos()
            elif escolha == '8':
                self.__menu_relatorios()
            elif escolha == '0':
                break  # sai do laco -> programa encerra
            else:
                self.__view_iniciar.opcao_invalida()

    # ---- SUBMENUS (cada um roteia para o controller da area) ----

    def __menu_atendimento(self):
        while True:
            escolha = self.__view_iniciar.submenu(
                "ATENDIMENTO", ["Registrar atendimento", "Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__registrar_atendimento()
            elif escolha == '2':
                self.__registro_atendimento_controller.listar()
            elif escolha == '3':
                self.__registro_atendimento_controller.alterar()
            elif escolha == '4':
                self.__registro_atendimento_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_clinicas(self):
        # cadastro de clinica acontece no fluxo de atendimento (quando nao existe);
        # aqui ficam listar/alterar/excluir.
        while True:
            escolha = self.__view_iniciar.submenu(
                "CLINICAS", ["Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__cadastrar_clinica_controller.listar()
            elif escolha == '2':
                self.__cadastrar_clinica_controller.alterar()
            elif escolha == '3':
                self.__cadastrar_clinica_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_pacientes(self):
        # cadastro de paciente acontece no fluxo de atendimento; aqui o resto do CRUD.
        while True:
            escolha = self.__view_iniciar.submenu(
                "PACIENTES", ["Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__cadastrar_paciente_controller.listar()
            elif escolha == '2':
                self.__cadastrar_paciente_controller.alterar()
            elif escolha == '3':
                self.__cadastrar_paciente_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_profissionais(self):
        while True:
            escolha = self.__view_iniciar.submenu(
                "PROFISSIONAIS", ["Cadastrar", "Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__cadastrar_profissional_controller.cadastrar()
            elif escolha == '2':
                self.__cadastrar_profissional_controller.listar()
            elif escolha == '3':
                self.__cadastrar_profissional_controller.alterar()
            elif escolha == '4':
                self.__cadastrar_profissional_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_tipos(self):
        while True:
            escolha = self.__view_iniciar.submenu(
                "TIPOS DE ATENDIMENTO", ["Cadastrar", "Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__cadastrar_tipo_atendimento_controller.cadastrar()
            elif escolha == '2':
                self.__cadastrar_tipo_atendimento_controller.listar()
            elif escolha == '3':
                self.__cadastrar_tipo_atendimento_controller.alterar()
            elif escolha == '4':
                self.__cadastrar_tipo_atendimento_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_procedimentos(self):
        while True:
            escolha = self.__view_iniciar.submenu(
                "PROCEDIMENTOS", ["Registrar", "Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__registro_procedimento_controller.registrar()
            elif escolha == '2':
                self.__registro_procedimento_controller.listar()
            elif escolha == '3':
                self.__registro_procedimento_controller.alterar()
            elif escolha == '4':
                self.__registro_procedimento_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_pagamentos(self):
        while True:
            escolha = self.__view_iniciar.submenu(
                "PAGAMENTOS", ["Registrar", "Listar", "Alterar", "Excluir"])
            if escolha == '1':
                self.__registro_pagamento_controller.registrar()
            elif escolha == '2':
                self.__registro_pagamento_controller.listar()
            elif escolha == '3':
                self.__registro_pagamento_controller.alterar()
            elif escolha == '4':
                self.__registro_pagamento_controller.excluir()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    def __menu_relatorios(self):
        while True:
            escolha = self.__view_iniciar.submenu("RELATORIOS", [
                "Procedimentos mais realizados",
                "Procedimentos mais caros e mais baratos",
                "Clinicas com mais atendimentos",
                "Atendimentos mais caros e mais baratos",
            ])
            if escolha == '1':
                self.__relatorio_controller.procedimentos_mais_realizados()
            elif escolha == '2':
                self.__relatorio_controller.procedimentos_caros_baratos()
            elif escolha == '3':
                self.__relatorio_controller.clinicas_mais_atendimentos()
            elif escolha == '4':
                self.__relatorio_controller.atendimentos_caros_baratos()
            elif escolha == '0':
                break
            else:
                self.__view_iniciar.opcao_invalida()

    # ---- helpers do atendimento ----

    def __registrar_atendimento(self):
        # valida a idade ANTES de seguir; so maior de 18 registra de forma independente
        idade = self.__ler_idade()
        if self.valida_idade(idade):
            self.__registro_atendimento_controller.iniciar_registro()
        else:
            self.__view_iniciar.invalida_atendimento()

    def __ler_idade(self):
        # le a idade e repete ate ser um inteiro valido.
        # try/except trata a entrada invalida (ex.: "abc" faria int() lancar ValueError).
        while True:
            idade = self.__view_iniciar.idade_user()
            try:
                return int(idade)
            except ValueError:
                self.__view_iniciar.erro_idade_invalida()

    def valida_idade(self, idade: int):
        # regra de negocio: so maior de 18 pode atendimento independente
        return idade >= 18
