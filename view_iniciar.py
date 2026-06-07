class ViewIniciar:
    def menu(self):
        print("TELA DE ATENDIMENTO")
        print("1 - Registrar atendimento")
        print("2 - Cadastrar paciente")
        print("3 - Cadastrar clínica")
        print("4 - Cadastrar profissional de saúde")
        print("5 - Listar clinicas")
        print("6 - Listar pacientes")
        print("7 - Encerrar")
        return input("Escolha um numero: ")
    
    def idade_user(self):
        print("VALIDAÇÃO IDADE PARA REGISTRAR ATENDIMENTO")
        return input("Idade: ")

    def invalida_atendimento(self):
        print("MENORES PRECISAM QUE UM RESPONSÁVEL REGISTRE O ATENDIMENTO")

    def erro_idade_invalida(self):
        print("Idade invalida: digite apenas numeros inteiros.")

    def opcao_invalida(self):
        print("Opcao invalida. Escolha um numero do menu.")
