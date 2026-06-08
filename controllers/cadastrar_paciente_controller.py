# CONTROLLER de cadastro de paciente (MVC) - CRUD completo de Paciente.
# Pacientes ficam DENTRO de cada clinica (clinica.pacientes), nao em lista global;
# por isso buscas/listagens varrem todas as clinicas do sistema.
from views.view_cadastrar_paciente import ViewCadastrarPaciente
from models.paciente import Paciente


class CadastrarPacienteController:
    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_paciente = ViewCadastrarPaciente()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def cadastrar(self, clinica, nome_paciente):
        # INCLUIR: o nome ja vem do fluxo; coleta os campos numericos (validados),
        # cria o Paciente e o adiciona a clinica recebida.
        self.__view_cadastrar_paciente.cabecalho_cadastro()
        celular = self.__ler_somente_numeros(self.__view_cadastrar_paciente.celular)
        cpf = self.__ler_somente_numeros(self.__view_cadastrar_paciente.cpf)
        data_nascimento = self.__ler_somente_numeros(self.__view_cadastrar_paciente.data_nascimento)
        paciente = Paciente(nome_paciente, celular, cpf, data_nascimento)
        clinica.pacientes = paciente  # setter da Clinica faz o append na lista
        return paciente

    def __ler_somente_numeros(self, metodo_view):
        # le de um metodo da tela e repete ate o valor ter SO digitos.
        # isdigit() (e nao int()) preserva zeros a esquerda de cpf/celular.
        valor = metodo_view()
        while not valor.isdigit():
            self.__view_cadastrar_paciente.erro_apenas_numeros()
            valor = metodo_view()
        return valor

    def listar(self):
        # LISTAR: varre todas as clinicas e seus pacientes, montando as linhas
        linhas = []
        for clinica in self.__sistema_clinicas.clinicas:
            for paciente in clinica.pacientes:
                linhas.append(
                    f"{paciente.nome} | cel: {paciente.celular} | cpf: {paciente.cpf} "
                    f"| nasc: {paciente.data_nascimento} | clinica: {clinica.nome}"
                )
        self.__view_cadastrar_paciente.listar_pacientes(linhas)

    def alterar(self):
        # ALTERAR: acha o paciente e atualiza os campos numericos (revalidados).
        # So precisamos do paciente aqui, entao ignoramos a clinica do retorno (_).
        resultado = self.__buscar_paciente()
        if resultado is None:
            return
        _, paciente = resultado
        paciente.celular = self.__ler_somente_numeros(self.__view_cadastrar_paciente.celular)
        paciente.cpf = self.__ler_somente_numeros(self.__view_cadastrar_paciente.cpf)
        paciente.data_nascimento = self.__ler_somente_numeros(self.__view_cadastrar_paciente.data_nascimento)
        self.__view_cadastrar_paciente.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: precisa da clinica (onde o paciente mora) para remove-lo de la
        resultado = self.__buscar_paciente()
        if resultado is None:
            return
        clinica, paciente = resultado
        clinica.remover_paciente(paciente)
        self.__view_cadastrar_paciente.sucesso_exclusao()

    def __buscar_paciente(self):
        # helper: pede o nome e procura em todas as clinicas.
        # Retorna a TUPLA (clinica, paciente) porque excluir precisa saber de qual
        # clinica remover. Trata nao encontrado (avisa e retorna None).
        nome = self.__view_cadastrar_paciente.pedir_nome()
        for clinica in self.__sistema_clinicas.clinicas:
            for paciente in clinica.pacientes:
                if paciente.nome == nome:
                    return (clinica, paciente)
        self.__view_cadastrar_paciente.nao_encontrado()
        return None
