# DAO de ProfissionalSaude: indexa por 'cpf' (chave natural, informada no
# cadastro) - catalogo global, cpf unico no sistema.
from daos.dao import DAO
from models.profissional_saude import ProfissionalSaude


class ProfissionalSaudeDAO(DAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional):
        if isinstance(profissional, ProfissionalSaude):
            super().add(profissional.cpf, profissional)
