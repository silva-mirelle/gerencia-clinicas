# DAO de Atendimento: indexa por 'codigo' (chave artificial sequencial).
# Procedimentos e pagamentos vivem dentro do atendimento -> persistem junto.
from daos.dao import DAO
from models.atendimento import Atendimento


class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento):
        if isinstance(atendimento, Atendimento):
            if atendimento.codigo is None:
                atendimento.codigo = self._proximo_codigo()
            super().add(atendimento.codigo, atendimento)
