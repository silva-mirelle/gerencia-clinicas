# VIEW (Tela) do registro de atendimento (MVC).
# So coleta texto do usuario e exibe mensagens; devolve as strings ao controller.
class ViewRegistroAtendimento:

    def nome_clinica(self):
        print("REGISTRO ATENDIMENTO")
        return input("Nome Clinica: ")

    def nome_paciente(self):
        return input("Nome Paciente: ")

    def nome_profissional(self):
        return input("Nome Profissional: ")

    def data_atendimento(self):
        return input("Data do atendimento: ")

    def horario_inicio(self):
        return input("Horario inicio do atendimento: ")

    def horario_fim(self):
        return input("Horario fim do atendimento: ")

    def tipo_atendimento(self):
        return input("Tipo de atendimento: ")

    def valor(self):
        return input("Valor do atendimento: ")

    def profissional_nao_cadastrado(self):
        print("Profissional nao cadastrado. Cadastre o profissional (opcao 4) antes do atendimento.")

    def erro_valor_invalido(self):
        print("Valor invalido: digite um numero (ex.: 150 ou 150.50).")

    def sucesso_registro(self):
        print("Atendimento registrado com sucesso.")
