# VIEW (Tela) do registro de pagamento (MVC). So entrada/saida.
class ViewRegistroPagamento:

    def selecionar_atendimento(self, linhas):
        # atendimentos numerados (nao tem "nome"); devolve o numero digitado
        print("---- ATENDIMENTOS ----")
        for i, linha in enumerate(linhas):
            print(f"{i + 1} - {linha}")
        return input("Numero do atendimento: ")

    def sem_atendimentos(self):
        print("Nenhum atendimento registrado. Registre um atendimento antes.")

    def selecao_invalida(self):
        print("Selecao invalida.")

    def escolher_modalidade(self):
        print("Modalidade de pagamento:")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartao de credito")
        return input("Escolha: ")

    def modalidade_invalida(self):
        print("Modalidade invalida.")

    def data_pagamento(self):
        return input("Data do pagamento: ")

    def valor_pago(self):
        return input("Valor pago: ")

    def erro_valor_invalido(self):
        print("Valor invalido: digite um numero (ex.: 50 ou 50.50).")

    def cpf_pagador(self):
        return input("CPF do pagador: ")

    def numero_cartao(self):
        return input("Numero do cartao: ")

    def bandeira(self):
        return input("Bandeira do cartao: ")

    def sucesso(self, restante):
        # mostra o restante -> evidencia o parcelamento (quanto ainda falta pagar)
        print(f"Pagamento registrado. Valor restante do atendimento: R$ {restante}")

    def listar_pagamentos(self, linhas):
        print("---- PAGAMENTOS ----")
        if not linhas:
            print("Nenhum pagamento registrado.")
        for linha in linhas:
            print(f"- {linha}")

    def selecionar_pagamento(self, linhas):
        # pagamentos do atendimento, numerados; devolve o numero digitado
        print("---- PAGAMENTOS DO ATENDIMENTO ----")
        for i, linha in enumerate(linhas):
            print(f"{i + 1} - {linha}")
        return input("Numero do pagamento: ")

    def sem_pagamentos(self):
        print("Este atendimento nao tem pagamentos.")

    def sucesso_alteracao(self):
        print("Pagamento alterado com sucesso.")

    def sucesso_exclusao(self):
        print("Pagamento excluido com sucesso.")
