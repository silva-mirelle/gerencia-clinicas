# DAO (Data Access Object) abstrato - camada de persistencia via serializacao.
# Guarda os objetos num __cache (dicionario chave->objeto) e o espelha em disco
# com pickle. Cada subclasse concreta define o arquivo (datasource) e o criterio
# de indexacao (qual atributo vira a chave). Classe base generica: NAO deve ser
# instanciada diretamente.
from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource  # nome do arquivo .pkl
        self.__cache = {}               # {chave: objeto} em memoria
        try:
            self.__load()               # tenta recuperar o que ja foi persistido
        except FileNotFoundError:
            self.__dump()               # primeira execucao: cria o arquivo vazio

    def __dump(self):
        # grava o cache inteiro no arquivo binario (with garante flush/close,
        # evitando .pkl truncado se o processo terminar antes do GC).
        with open(self.__datasource, 'wb') as arquivo:
            pickle.dump(self.__cache, arquivo)

    def __load(self):
        with open(self.__datasource, 'rb') as arquivo:
            self.__cache = pickle.load(arquivo)

    def add(self, key, obj):
        # inclui/atualiza pela chave e persiste a cada alteracao
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        # EAFP: tenta pegar e trata a ausencia, em vez de checar antes
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()

    def _proximo_codigo(self):
        # chave artificial sequencial: maior codigo ja usado + 1 (1 se vazio).
        # protegido (_) para as subclasses de chave artificial reaproveitarem.
        return max(self.__cache.keys(), default=0) + 1
