# DAO de Clinica: config do GenericDAO. Indexa por 'codigo' (chave artificial
# sequencial). Pacientes vivem dentro da clinica -> persistem junto (transitivo).
from daos.generic_dao import GenericDAO
from models.clinica import Clinica


class ClinicaDAO(GenericDAO):
    def __init__(self):
        super().__init__('clinicas.pkl', Clinica, 'codigo', auto_code=True)
