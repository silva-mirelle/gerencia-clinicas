# CONTROLLER de cadastro de profissional de saude (MVC) - CRUD completo.
# Profissionais ficam numa lista global no SistemaClinicas (catalogo do sistema),
# do mesmo jeito que os tipos de atendimento.
from view_cadastrar_profissional import ViewCadastrarProfissional
from profissional_saude import ProfissionalSaude
from validacao import ler_obrigatorio


class CadastrarProfissionalController:

    def __init__(self, sistema_clinicas):
        self.__view_cadastrar_profissional = ViewCadastrarProfissional()
        self.__sistema_clinicas = sistema_clinicas  # sistema compartilhado (injetado)

    def cadastrar(self):
        # INCLUIR: coleta os campos, cria o ProfissionalSaude e guarda no sistema.
        # celular e cpf passam pela validacao de "somente numeros".
        self.__view_cadastrar_profissional.cabecalho_cadastro()
        nome = ler_obrigatorio(self.__view_cadastrar_profissional.nome,
                               self.__view_cadastrar_profissional.erro_campo_obrigatorio)
        celular = self.__ler_somente_numeros(self.__view_cadastrar_profissional.celular)
        cpf = self.__ler_somente_numeros(self.__view_cadastrar_profissional.cpf)
        especialidade = ler_obrigatorio(self.__view_cadastrar_profissional.especialidade,
                                        self.__view_cadastrar_profissional.erro_campo_obrigatorio)
        registro = ler_obrigatorio(self.__view_cadastrar_profissional.registro_profissional,
                                   self.__view_cadastrar_profissional.erro_campo_obrigatorio)
        profissional = ProfissionalSaude(nome, celular, cpf, especialidade, registro)
        self.__sistema_clinicas.registrar_profissional(profissional)
        return profissional

    def listar(self):
        # LISTAR: monta as linhas de texto e manda a tela exibir
        linhas = [
            f"{p.nome} | cel: {p.celular} | cpf: {p.cpf} "
            f"| esp: {p.especialidade} | reg: {p.registro_profissional}"
            for p in self.__sistema_clinicas.profissionais
        ]
        self.__view_cadastrar_profissional.listar_profissionais(linhas)

    def alterar(self):
        # ALTERAR: acha pelo nome e atualiza especialidade e registro profissional
        profissional = self.__buscar_profissional()
        if profissional is None:
            return
        dados = self.__view_cadastrar_profissional.pegar_dados_alteracao()
        profissional.especialidade = dados["especialidade"]
        profissional.registro_profissional = dados["registro_profissional"]
        self.__view_cadastrar_profissional.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: acha pelo nome e remove do sistema
        profissional = self.__buscar_profissional()
        if profissional is None:
            return
        self.__sistema_clinicas.remover_profissional(profissional)
        self.__view_cadastrar_profissional.sucesso_exclusao()

    def __buscar_profissional(self):
        # helper: pede o nome e procura; trata nao encontrado (avisa e retorna None)
        nome = self.__view_cadastrar_profissional.pedir_nome()
        for profissional in self.__sistema_clinicas.profissionais:
            if profissional.nome == nome:
                return profissional
        self.__view_cadastrar_profissional.nao_encontrado()
        return None

    def __ler_somente_numeros(self, metodo_view):
        # repete ate o usuario digitar so numeros (mesma validacao do paciente)
        valor = metodo_view()
        while not valor.isdigit():
            self.__view_cadastrar_profissional.erro_apenas_numeros()
            valor = metodo_view()
        return valor
