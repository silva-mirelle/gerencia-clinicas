class SistemaClinicas:
    def __init__(self):
        self.__clinicas = []

    @property
    def clinicas(self):
        return self.__clinicas
    
    @clinicas.setter
    def clinicas(self, clinicas):
        self.__clinicas = clinicas

    def registrar_clinica(self, clinica):
        self.__clinicas.append(clinica)
        print("----CLINICA REGISTRADA COM SUCESSO----")

    def remover_clinica(self, clinica):
        self.__clinicas.remove(clinica)