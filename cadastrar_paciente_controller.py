from view_cadastrar_paciente import ViewCadastrarPaciente
from paciente import Paciente

class CadastrarPacienteController:
    def __init__(self):
        self.__view_cadastrar_paciente = ViewCadastrarPaciente()
    
    def cadastrar(self, clinica, nome_paciente):
        nome = nome_paciente
        celular = self.__ler_somente_numeros(self.__view_cadastrar_paciente.celular)
        cpf = self.__ler_somente_numeros(self.__view_cadastrar_paciente.cpf)
        data_nascimento = self.__ler_somente_numeros(self.__view_cadastrar_paciente.data_nascimento)
        paciente = Paciente(nome, celular, cpf, data_nascimento)
        clinica.pacientes = paciente
        return paciente

    def __ler_somente_numeros(self, metodo_view):
        valor = metodo_view()
        while not valor.isdigit():
            self.__view_cadastrar_paciente.erro_apenas_numeros()
            valor = metodo_view()
        return valor
