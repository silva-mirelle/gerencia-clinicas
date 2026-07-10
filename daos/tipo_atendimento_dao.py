# DAO de TipoAtendimento: config do GenericDAO. Indexa por 'codigo' (artificial).
from daos.generic_dao import GenericDAO
from models.tipo_atendimento import TipoAtendimento


class TipoAtendimentoDAO(GenericDAO):
    def __init__(self):
        super().__init__('tipos_atendimento.pkl', TipoAtendimento, 'codigo', auto_code=True)
