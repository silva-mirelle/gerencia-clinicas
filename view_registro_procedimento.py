# VIEW (Tela) do registro de procedimento (MVC). So entrada/saida.
class ViewRegistroProcedimento:

    def selecionar_atendimento(self, linhas):
        # mostra os atendimentos NUMERADOS (atendimento nao tem "nome") e
        # devolve o numero digitado (string) pro controller validar
        print("---- ATENDIMENTOS ----")
        for i, linha in enumerate(linhas):
            print(f"{i + 1} - {linha}")
        return input("Numero do atendimento: ")

    def sem_atendimentos(self):
        print("Nenhum atendimento registrado. Registre um atendimento antes.")

    def selecao_invalida(self):
        print("Selecao invalida.")

    def descricao(self):
        return input("Descricao do procedimento: ")

    def custo(self):
        return input("Custo do procedimento: ")

    def erro_custo_invalido(self):
        print("Custo invalido: digite um numero (ex.: 80 ou 80.50).")

    def nome_profissional(self):
        return input("Profissional que executou (nome): ")

    def profissional_nao_cadastrado(self):
        print("Profissional nao cadastrado. Cadastre o profissional (opcao 4) antes.")

    def sucesso(self):
        print("Procedimento registrado com sucesso.")

    def listar_procedimentos(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- PROCEDIMENTOS ----")
        if not linhas:
            print("Nenhum procedimento registrado.")
        for linha in linhas:
            print(f"- {linha}")
