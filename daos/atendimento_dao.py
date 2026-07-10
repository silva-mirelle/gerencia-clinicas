# DAO de Atendimento: config do GenericDAO. Indexa por 'codigo' (artificial).
# Procedimentos e pagamentos vivem dentro do atendimento -> persistem junto.
from daos.generic_dao import GenericDAO
from models.atendimento import Atendimento


class AtendimentoDAO(GenericDAO):
    def __init__(self):
        super().__init__('atendimentos.pkl', Atendimento, 'codigo', auto_code=True)
