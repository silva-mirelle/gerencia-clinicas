# VIEW (Tela) do menu principal (MVC).
# So faz entrada/saida. O menu agora e em 2 niveis: um menu principal por AREA
# e submenus com as acoes de cada area (deixa o menu enxuto).
class ViewIniciar:

    def menu(self):
        # menu principal: so as AREAS (o detalhe fica nos submenus)
        print("\n=== SISTEMA DE CLINICAS ===")
        print("1 - Atendimento")
        print("2 - Clinicas")
        print("3 - Pacientes")
        print("4 - Profissionais")
        print("5 - Tipos de atendimento")
        print("6 - Procedimentos")
        print("7 - Pagamentos")
        print("8 - Relatorios")
        print("0 - Encerrar")
        return input("Escolha: ")

    def submenu(self, titulo, opcoes):
        # submenu generico: recebe o titulo e a lista de acoes, numera e le a escolha.
        # "0 - Voltar" volta pro menu principal.
        print(f"\n--- {titulo} ---")
        for i, opcao in enumerate(opcoes):
            print(f"{i + 1} - {opcao}")
        print("0 - Voltar")
        return input("Escolha: ")

    def idade_user(self):
        # pede a idade (validacao numerica e feita no controller)
        print("VALIDACAO DE IDADE PARA REGISTRAR ATENDIMENTO")
        return input("Idade: ")

    def invalida_atendimento(self):
        print("MENORES PRECISAM QUE UM RESPONSAVEL REGISTRE O ATENDIMENTO")

    def erro_idade_invalida(self):
        print("Idade invalida: digite apenas numeros inteiros.")

    def opcao_invalida(self):
        print("Opcao invalida. Escolha um numero do menu.")
