# VIEW (Tela) do cadastro de tipo de atendimento (MVC). So entrada/saida.
class ViewCadastrarTipoAtendimento:

    def pegar_nome(self):
        # usado no cadastro (com cabecalho)
        print("VAMOS CADASTRAR O TIPO DE ATENDIMENTO")
        return input("Nome do tipo de atendimento: ")

    def pedir_nome(self):
        # usado para selecionar o tipo em alterar/excluir
        return input("Nome do tipo de atendimento: ")

    def novo_nome(self):
        # usado na alteracao
        return input("Novo nome do tipo de atendimento: ")

    def listar_tipos(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- TIPOS DE ATENDIMENTO ----")
        if not linhas:
            print("Nenhum tipo de atendimento cadastrado.")
        for linha in linhas:
            print(f"- {linha}")

    def nao_encontrado(self):
        print("Tipo de atendimento nao encontrado.")

    def sucesso_alteracao(self):
        print("Tipo de atendimento alterado com sucesso.")

    def sucesso_exclusao(self):
        print("Tipo de atendimento excluido com sucesso.")
