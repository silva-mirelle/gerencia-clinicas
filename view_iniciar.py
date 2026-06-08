# VIEW (Tela) do menu principal (MVC).
# So faz entrada/saida com o usuario (print/input). Nenhuma regra de negocio:
# quem decide o que cada opcao faz e o IniciarController.
class ViewIniciar:
    def menu(self):
        # mostra as opcoes e devolve a escolha (string) ao controller
        print("TELA DE ATENDIMENTO")
        print("1 - Registrar atendimento")
        print("2 - Cadastrar paciente")
        print("3 - Cadastrar clínica")
        print("4 - Cadastrar profissional de saúde")
        print("5 - Listar clinicas")
        print("6 - Listar pacientes")
        print("7 - Alterar clinica")
        print("8 - Excluir clinica")
        print("9 - Alterar paciente")
        print("10 - Excluir paciente")
        print("11 - Cadastrar tipo de atendimento")
        print("12 - Listar tipos de atendimento")
        print("13 - Alterar tipo de atendimento")
        print("14 - Excluir tipo de atendimento")
        print("15 - Listar profissionais")
        print("16 - Alterar profissional")
        print("17 - Excluir profissional")
        print("18 - Registrar procedimento")
        print("19 - Listar procedimentos")
        print("20 - Relatorio: procedimentos mais realizados")
        print("21 - Relatorio: procedimentos mais caros e mais baratos")
        print("22 - Registrar pagamento")
        print("23 - Listar pagamentos")
        print("24 - Listar atendimentos")
        print("25 - Alterar atendimento")
        print("26 - Excluir atendimento")
        print("27 - Alterar procedimento")
        print("28 - Excluir procedimento")
        print("0 - Encerrar")
        return input("Escolha um numero: ")

    def idade_user(self):
        # pede a idade (validacao numerica e feita no controller)
        print("VALIDAÇÃO IDADE PARA REGISTRAR ATENDIMENTO")
        return input("Idade: ")

    def invalida_atendimento(self):
        print("MENORES PRECISAM QUE UM RESPONSÁVEL REGISTRE O ATENDIMENTO")

    def erro_idade_invalida(self):
        print("Idade invalida: digite apenas numeros inteiros.")

    def opcao_invalida(self):
        print("Opcao invalida. Escolha um numero do menu.")
