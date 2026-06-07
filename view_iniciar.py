class TelaAtendimento:
    def menu(self):
        print("TELA DE ATENDIMENTO")
        print("1 - Registrar atendimento")
        print("2 - Cadastrar paciente")
        print("3 - Cadastrar clínica")
        print("4 - Cadastrar profissional de saúde")
        print("5 - Encerrar")
        return input("Escolha um numero: ")
    
    def idade_user(self):
        print("VALIDAÇÃO IDADE PARA REGISTRAR ATENDIMENTO")
        return input("Idade: ")

    def invalida_atendimento(self):
        print("MENORES PRECISAM QUE UM RESPONSÁVEL REGISTRE O ATENDIMENTO")

    def dados_registro_atendimento(self):
        print("REGISTRO ATENDIMENTO")
        clinica = input("Nome Clinica: ")
        paciente = input("Nome Paciente: ")
        profissional = input("Nome Profissional: ")
        data = input("Data do atendimento: ")
        horario_inicio = input("Horario inicio do atendimento: ")
        horario_fim = input("Horario fim do atendimento: ")
        tipo_atend = input("Tipo do atendimento: ")

'''def dados_registro_atendimento(self):
        print("REGISTRO ATENDIMENTO")
        paciente = input("Nome Paciente: ")
        profissional = input("Nome Profissional: ")
        data = input("Data do atendimento: ")
        horario_inicio = input("Horario inicio do atendimento: ")
        horario_fim = input("Horario fim do atendimento: ")
        tipo_atend = input("Tipo do atendimento: ")'''