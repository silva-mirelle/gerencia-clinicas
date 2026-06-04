from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def forma(self):
        return "Dinheiro"
