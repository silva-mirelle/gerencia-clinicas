from view_cadastrar_paciente import ViewCadastrarPaciente
from paciente import Paciente

class CadastrarPacienteController:
    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_paciente = ViewCadastrarPaciente()
        self.__sistema_clinicas = sistema_clinicas
    
    def cadastrar(self, clinica, nome_paciente):
        self.__view_cadastrar_paciente.cabecalho_cadastro()
        celular = self.__ler_somente_numeros(self.__view_cadastrar_paciente.celular)
        cpf = self.__ler_somente_numeros(self.__view_cadastrar_paciente.cpf)
        data_nascimento = self.__ler_somente_numeros(self.__view_cadastrar_paciente.data_nascimento)
        paciente = Paciente(nome_paciente, celular, cpf, data_nascimento)
        clinica.pacientes = paciente
        return paciente

    def __ler_somente_numeros(self, metodo_view):
        valor = metodo_view()
        while not valor.isdigit():
            self.__view_cadastrar_paciente.erro_apenas_numeros()
            valor = metodo_view()
        return valor

    def listar(self):
        linhas = []
        for clinica in self.__sistema_clinicas.clinicas:
            for paciente in clinica.pacientes:
                linhas.append(
                    f"{paciente.nome} | cel: {paciente.celular} | cpf: {paciente.cpf} "
                    f"| nasc: {paciente.data_nascimento} | clinica: {clinica.nome}"
                )
        self.__view_cadastrar_paciente.listar_pacientes(linhas)

    def alterar(self):
        resultado = self.__buscar_paciente()
        if resultado is None:
            return
        _, paciente = resultado
        paciente.celular = self.__ler_somente_numeros(self.__view_cadastrar_paciente.celular)
        paciente.cpf = self.__ler_somente_numeros(self.__view_cadastrar_paciente.cpf)
        paciente.data_nascimento = self.__ler_somente_numeros(self.__view_cadastrar_paciente.data_nascimento)
        self.__view_cadastrar_paciente.sucesso_alteracao()

    def excluir(self):
        resultado = self.__buscar_paciente()
        if resultado is None:
            return
        clinica, paciente = resultado
        clinica.remover_paciente(paciente)
        self.__view_cadastrar_paciente.sucesso_exclusao()

    def __buscar_paciente(self):
        nome = self.__view_cadastrar_paciente.pedir_nome()
        for clinica in self.__sistema_clinicas.clinicas:
            for paciente in clinica.pacientes:
                if paciente.nome == nome:
                    return (clinica, paciente)
        self.__view_cadastrar_paciente.nao_encontrado()
        return None
