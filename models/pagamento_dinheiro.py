# MODEL. Pagamento em dinheiro - E-UM Pagamento (heranca).
# Nao precisa de atributos extras; so implementa forma().
from models.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def forma(self):
        return "Dinheiro"
