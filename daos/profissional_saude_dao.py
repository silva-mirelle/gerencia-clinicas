# DAO de ProfissionalSaude: config do GenericDAO. Indexa por 'cpf' (chave
# natural, informada no cadastro) - catalogo global, cpf unico no sistema.
from daos.generic_dao import GenericDAO
from models.profissional_saude import ProfissionalSaude


class ProfissionalSaudeDAO(GenericDAO):
    def __init__(self):
        super().__init__('profissionais.pkl', ProfissionalSaude, 'cpf')
