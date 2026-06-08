# VIEW (Tela) do cadastro de paciente (MVC). So entrada/saida.
class ViewCadastrarPaciente:

    def cabecalho_cadastro(self):
        # cabecalho separado do input para poder reaproveitar celular/cpf/data
        # tambem na ALTERACAO sem repetir "VAMOS CADASTRAR".
        print("VAMOS CADASTRAR O PACIENTE - JA TEMOS O NOME")
        print("---- AGORA INDIQUE ----")

    def celular(self):
        return input("Celular (somente numeros): ")

    def cpf(self):
        return input("CPF (somente numeros): ")

    def data_nascimento(self):
        return input("Data de nascimento (somente numeros): ")

    def erro_apenas_numeros(self):
        print("Entrada invalida: use apenas numeros (0-9), sem espacos, letras ou simbolos.")

    def listar_pacientes(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- PACIENTES ----")
        if not linhas:
            print("Nenhum paciente cadastrado.")
        for linha in linhas:
            print(f"- {linha}")

    def pedir_nome(self):
        # usado para selecionar o paciente em alterar/excluir
        return input("Nome do paciente: ")

    def nao_encontrado(self):
        print("Paciente nao encontrado.")

    def sucesso_alteracao(self):
        print("Paciente alterado com sucesso.")

    def sucesso_exclusao(self):
        print("Paciente excluido com sucesso.")
