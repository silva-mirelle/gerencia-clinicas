# DAO de Clinica: indexa por 'codigo' (chave artificial sequencial). Pacientes
# vivem dentro da clinica -> persistem junto (transitivo).
from daos.dao import DAO
from models.clinica import Clinica


class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica):
        if isinstance(clinica, Clinica):
            if clinica.codigo is None:
                clinica.codigo = self._proximo_codigo()
            super().add(clinica.codigo, clinica)
