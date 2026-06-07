# VIEW (Tela) do registro de atendimento (MVC).
# So coleta texto do usuario e exibe mensagens; devolve as strings ao controller.
class ViewRegistroAtendimento:

    def nome_clinica(self):
        print("REGISTRO ATENDIMENTO")
        return input("Nome Clinica: ")

    def nome_paciente(self):
        return input("Nome Paciente: ")

    def nome_profissional(self):
        return input("Nome Profissional: ")

    def data_atendimento(self):
        return input("Data do atendimento: ")

    def horario_inicio(self):
        return input("Horario inicio do atendimento: ")

    def horario_fim(self):
        return input("Horario fim do atendimento: ")

    def tipo_atendimento(self):
        return input("Tipo de atendimento: ")

    def valor(self):
        return input("Valor do atendimento: ")

    def profissional_nao_cadastrado(self):
        print("Profissional nao cadastrado. Cadastre o profissional (opcao 4) antes do atendimento.")

    def erro_valor_invalido(self):
        print("Valor invalido: digite um numero (ex.: 150 ou 150.50).")

    def sucesso_registro(self):
        print("Atendimento registrado com sucesso.")

    def selecionar_atendimento(self, linhas):
        # atendimentos numerados (nao tem nome); devolve o numero digitado
        print("---- ATENDIMENTOS ----")
        for i, linha in enumerate(linhas):
            print(f"{i + 1} - {linha}")
        return input("Numero do atendimento: ")

    def sem_atendimentos(self):
        print("Nenhum atendimento registrado.")

    def selecao_invalida(self):
        print("Selecao invalida.")

    def listar_atendimentos(self, linhas):
        # recebe linhas ja prontas do controller e so imprime
        print("---- ATENDIMENTOS ----")
        if not linhas:
            print("Nenhum atendimento registrado.")
        for linha in linhas:
            print(f"- {linha}")

    def sucesso_alteracao(self):
        print("Atendimento alterado com sucesso.")

    def sucesso_exclusao(self):
        print("Atendimento excluido com sucesso.")
