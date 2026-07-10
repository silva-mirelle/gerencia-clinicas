# DAO de TipoAtendimento: indexa por 'codigo' (chave artificial sequencial).
from daos.dao import DAO
from models.tipo_atendimento import TipoAtendimento


class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('tipos_atendimento.pkl')

    def add(self, tipo_atendimento):
        if isinstance(tipo_atendimento, TipoAtendimento):
            if tipo_atendimento.codigo is None:
                tipo_atendimento.codigo = self._proximo_codigo()
            super().add(tipo_atendimento.codigo, tipo_atendimento)
