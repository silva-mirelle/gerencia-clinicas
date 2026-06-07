# VIEW (Tela) do cadastro de profissional de saude (MVC). So entrada/saida.
class ViewCadastrarProfissional:

    def cabecalho_cadastro(self):
        print("VAMOS CADASTRAR O PROFISSIONAL DE SAUDE")

    def nome(self):
        return input("Nome: ")

    def celular(self):
        return input("Celular (somente numeros): ")

    def cpf(self):
        return input("CPF (somente numeros): ")

    def especialidade(self):
        return input("Especialidade: ")

    def registro_profissional(self):
        return input("Registro profissional: ")

    def erro_apenas_numeros(self):
        print("Entrada invalida: use apenas numeros (0-9), sem espacos, letras ou simbolos.")

    def listar_profissionais(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- PROFISSIONAIS ----")
        if not linhas:
            print("Nenhum profissional cadastrado.")
        for linha in linhas:
            print(f"- {linha}")

    def pedir_nome(self):
        # usado para selecionar o profissional em alterar/excluir
        return input("Nome do profissional: ")

    def pegar_dados_alteracao(self):
        # coleta os novos dados e devolve um dict pro controller
        print("Novos dados do profissional:")
        especialidade = input("Nova especialidade: ")
        registro_profissional = input("Novo registro profissional: ")
        return {"especialidade": especialidade, "registro_profissional": registro_profissional}

    def nao_encontrado(self):
        print("Profissional nao encontrado.")

    def sucesso_alteracao(self):
        print("Profissional alterado com sucesso.")

    def sucesso_exclusao(self):
        print("Profissional excluido com sucesso.")
