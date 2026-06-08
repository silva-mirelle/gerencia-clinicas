# VIEW (Tela) do cadastro de clinica (MVC). So entrada/saida.
class ViewCadastrarClinica:

    def localizacao(self):
        print("VAMOS CADASTRAR A CLÍNICA - JÁ TEMOS O NOME")
        print("AGORA INDIQUE O RESTO")
        return input("Localização da clinica: ")

    def descricao(self):
        return input("Descrição da clinica: ")

    def listar_clinicas(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- CLINICAS ----")
        if not linhas:
            print("Nenhuma clinica cadastrada.")
        for linha in linhas:
            print(f"- {linha}")

    def pedir_nome(self):
        # usado para selecionar a clinica em alterar/excluir
        return input("Nome da clinica: ")

    def pegar_dados_alteracao(self):
        # coleta os novos dados e devolve um dict pro controller
        print("Novos dados da clinica:")
        localizacao = input("Nova localizacao: ")
        descricao = input("Nova descricao: ")
        return {"localizacao": localizacao, "descricao": descricao}

    def nao_encontrada(self):
        print("Clinica nao encontrada.")

    def sucesso_alteracao(self):
        print("Clinica alterada com sucesso.")

    def sucesso_exclusao(self):
        print("Clinica excluida com sucesso.")

    def erro_campo_obrigatorio(self):
        print("Campo obrigatorio: nao pode ficar vazio.")
