# CONTROLLER de registro de procedimento (MVC).
# Um procedimento e registrado DENTRO de um atendimento (atendimento.procedimentos).
# Fluxo: escolhe o atendimento -> coleta dados -> cria Procedimento -> adiciona nele.
from view_registro_procedimento import ViewRegistroProcedimento
from procedimento import Procedimento


class RegistroProcedimentoController:

    def __init__(self, sistema_clinicas):
        self.__view_registro_procedimento = ViewRegistroProcedimento()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def registrar(self):
        # INCLUIR: escolhe o atendimento, coleta descricao/custo/profissional,
        # cria o Procedimento e adiciona ao atendimento escolhido.
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        descricao = self.__view_registro_procedimento.descricao()
        custo = self.__ler_custo()
        profissional = self.__valida_profissional()
        if profissional is None:
            self.__view_registro_procedimento.profissional_nao_cadastrado()
            return
        procedimento = Procedimento(descricao, custo, profissional)
        atendimento.adicionar_procedimento(procedimento)
        self.__view_registro_procedimento.sucesso()

    def listar(self):
        # LISTAR: percorre todos os atendimentos e seus procedimentos
        linhas = []
        for atendimento in self.__sistema_clinicas.atendimentos:
            for procedimento in atendimento.procedimentos:
                linhas.append(
                    f"{procedimento.descricao} | custo: {procedimento.custo} "
                    f"| prof: {procedimento.profissional.nome} "
                    f"| paciente: {atendimento.paciente.nome}"
                )
        self.__view_registro_procedimento.listar_procedimentos(linhas)

    def __selecionar_atendimento(self):
        # mostra os atendimentos numerados e valida o numero escolhido.
        # retorna o OBJETO Atendimento ou None (lista vazia / selecao invalida).
        atendimentos = self.__sistema_clinicas.atendimentos
        if not atendimentos:
            self.__view_registro_procedimento.sem_atendimentos()
            return None
        linhas = [f"{a.paciente.nome} | {a.clinica.nome} | {a.data}" for a in atendimentos]
        escolha = self.__view_registro_procedimento.selecionar_atendimento(linhas)
        if not escolha.isdigit():
            self.__view_registro_procedimento.selecao_invalida()
            return None
        indice = int(escolha) - 1  # usuario ve 1..N; lista e 0..N-1
        if indice < 0 or indice >= len(atendimentos):
            self.__view_registro_procedimento.selecao_invalida()
            return None
        return atendimentos[indice]

    def __valida_profissional(self):
        # o profissional executor precisa JA estar cadastrado (menu opcao 4)
        nome = self.__view_registro_procedimento.nome_profissional()
        for profissional in self.__sistema_clinicas.profissionais:
            if profissional.nome == nome:
                return profissional
        return None

    def __ler_custo(self):
        # le o custo e converte pra float; repete se nao for numero
        while True:
            try:
                return float(self.__view_registro_procedimento.custo())
            except ValueError:
                self.__view_registro_procedimento.erro_custo_invalido()

    def alterar(self):
        # ALTERAR: escolhe o atendimento -> escolhe o procedimento -> troca descricao/custo
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        procedimento = self.__selecionar_procedimento(atendimento)
        if procedimento is None:
            return
        procedimento.descricao = self.__view_registro_procedimento.descricao()
        procedimento.custo = self.__ler_custo()
        self.__view_registro_procedimento.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: escolhe o atendimento -> escolhe o procedimento -> remove do atendimento
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        procedimento = self.__selecionar_procedimento(atendimento)
        if procedimento is None:
            return
        atendimento.remover_procedimento(procedimento)
        self.__view_registro_procedimento.sucesso_exclusao()

    def __selecionar_procedimento(self, atendimento):
        # selecao numerada dos procedimentos DAQUELE atendimento; objeto ou None
        procedimentos = atendimento.procedimentos
        if not procedimentos:
            self.__view_registro_procedimento.sem_procedimentos()
            return None
        linhas = [f"{p.descricao} | custo: {p.custo} | prof: {p.profissional.nome}"
                  for p in procedimentos]
        escolha = self.__view_registro_procedimento.selecionar_procedimento(linhas)
        if not escolha.isdigit():
            self.__view_registro_procedimento.selecao_invalida()
            return None
        indice = int(escolha) - 1
        if indice < 0 or indice >= len(procedimentos):
            self.__view_registro_procedimento.selecao_invalida()
            return None
        return procedimentos[indice]
