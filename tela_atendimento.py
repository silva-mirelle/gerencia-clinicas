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
