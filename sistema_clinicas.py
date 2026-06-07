# "Banco de dados" em memoria do sistema (registro central).
# Guarda as listas de clinicas e de tipos de atendimento. Uma unica instancia e
# compartilhada por todos os controllers (criada no IniciarController).
class SistemaClinicas:
    def __init__(self):
        self.__clinicas = []           # lista de objetos Clinica
        self.__tipos_atendimento = []  # lista de objetos TipoAtendimento
        self.__profissionais = []      # lista de objetos ProfissionalSaude
        self.__atendimentos = []       # lista de objetos Atendimento (registros)

    @property
    def clinicas(self):
        return self.__clinicas

    @clinicas.setter
    def clinicas(self, clinicas):
        self.__clinicas = clinicas

    def registrar_clinica(self, clinica):
        # adiciona uma clinica e confirma na tela
        self.__clinicas.append(clinica)
        print("----CLINICA REGISTRADA COM SUCESSO----")

    def remover_clinica(self, clinica):
        self.__clinicas.remove(clinica)

    @property
    def tipos_atendimento(self):
        return self.__tipos_atendimento

    def registrar_tipo_atendimento(self, tipo):
        self.__tipos_atendimento.append(tipo)
        print("----TIPO DE ATENDIMENTO REGISTRADO COM SUCESSO----")

    def remover_tipo_atendimento(self, tipo):
        self.__tipos_atendimento.remove(tipo)

    @property
    def profissionais(self):
        return self.__profissionais

    def registrar_profissional(self, profissional):
        self.__profissionais.append(profissional)
        print("----PROFISSIONAL REGISTRADO COM SUCESSO----")

    def remover_profissional(self, profissional):
        self.__profissionais.remove(profissional)

    @property
    def atendimentos(self):
        return self.__atendimentos

    def registrar_atendimento(self, atendimento):
        self.__atendimentos.append(atendimento)

    def remover_atendimento(self, atendimento):
        self.__atendimentos.remove(atendimento)

    # ---- RELATORIOS (so computacao sobre os dados; quem exibe e o controller/view) ----

    def procedimentos_mais_realizados(self):
        # conta os procedimentos por descricao em TODOS os atendimentos.
        # retorna lista de (descricao, quantidade), da mais realizada pra menos.
        contagem = {}
        for atendimento in self.__atendimentos:
            for procedimento in atendimento.procedimentos:
                contagem[procedimento.descricao] = contagem.get(procedimento.descricao, 0) + 1
        return sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    def procedimentos_por_custo(self):
        # junta os procedimentos de todos os atendimentos e ordena por custo (crescente).
        # o controller usa o primeiro (mais barato) e o ultimo (mais caro).
        procedimentos = [p for a in self.__atendimentos for p in a.procedimentos]
        return sorted(procedimentos, key=lambda p: p.custo)
