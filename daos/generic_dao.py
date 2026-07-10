# DAO generico (resposta ao desafio "DAO Generico"). Fica entre o DAO abstrato
# (armazenamento + pickle) e os DAOs concretos: implementa UMA vez o add comum,
# parametrizado por configuracao. Cada DAO concreto vira so a config:
#   - datasource: arquivo .pkl
#   - cls: classe dos objetos (validacao de tipo no add)
#   - key_attr: atributo que indexa (ex.: 'codigo', 'cpf')
#   - auto_code: se True, gera key_attr sequencialmente quando ausente
from daos.dao import DAO


class GenericDAO(DAO):
    def __init__(self, datasource, cls, key_attr, auto_code=False):
        self.__cls = cls
        self.__key_attr = key_attr
        self.__auto_code = auto_code
        super().__init__(datasource)

    def add(self, obj):
        # valida o tipo; se a chave e artificial e ainda nao existe, gera uma
        # sequencial; indexa pelo atributo-chave configurado
        if isinstance(obj, self.__cls):
            if self.__auto_code and getattr(obj, self.__key_attr) is None:
                setattr(obj, self.__key_attr, self._proximo_codigo())
            super().add(getattr(obj, self.__key_attr), obj)

    # get / remove / get_all vem prontos do DAO base (agnosticos a chave)
