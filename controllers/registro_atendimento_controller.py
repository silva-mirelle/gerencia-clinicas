# CONTROLLER de registro de atendimento (MVC).
# Orquestra o fluxo de marcar um atendimento: valida/cadastra clinica e paciente,
# valida o profissional, coleta os dados, cria o Atendimento e guarda no sistema.
from views.view_registro_atendimento import ViewRegistroAtendimento
#from view_cadastrar_profissional import CadastrarProfissionalController
from models.atendimento import Atendimento
from models.tipo_atendimento import TipoAtendimento
from validacao import ler_obrigatorio


class RegistroAtendimentoController:

    # Recebe (injecao de dependencia) o sistema compartilhado e os controllers de
    # cadastro ja prontos, para reaproveitar clinica/paciente ja existentes.
    def __init__(self, sistema_clinicas, cadastrar_clinica_controller, cadastrar_paciente_controller):
        self.__view_registro_atendimento = ViewRegistroAtendimento()
        self.__sistema_clinicas = sistema_clinicas
        self.__cadastrar_clinica_controller = cadastrar_clinica_controller
        self.__cadastrar_paciente_controller = cadastrar_paciente_controller
        #self.__atendimentos = []

    def iniciar_registro(self):
        # passo a passo: clinica -> paciente -> profissional -> dados -> valor -> cria
        clinica = self.valida_clinica()
        paciente = self.valida_paciente(clinica)

        profissional = self.valida_profissional()
        if profissional is None:
            # regra: o profissional precisa estar cadastrado antes (menu opcao 4).
            # sem profissional, aborta o registro e volta ao menu.
            self.__view_registro_atendimento.profissional_nao_cadastrado()
            return

        dados = self.coletar_dados_atendimento()
        valor = self.__ler_valor()

        # cria o Atendimento com tudo coletado e guarda no sistema
        atendimento = Atendimento(
            clinica, paciente, profissional,
            dados["data"], dados["horario_inicio"], dados["horario_fim"],
            dados["tipo_atendimento"], valor,
        )
        self.__sistema_clinicas.registrar_atendimento(atendimento)
        self.__view_registro_atendimento.sucesso_registro()

    def coletar_dados_atendimento(self):
        # coleta os campos proprios do atendimento via tela e devolve um dict pronto
        data = self.__view_registro_atendimento.data_atendimento()
        horario_inicio = self.__view_registro_atendimento.horario_inicio()
        horario_fim = self.__view_registro_atendimento.horario_fim()
        nome_tipo = self.__view_registro_atendimento.tipo_atendimento()
        tipo_atendimento = TipoAtendimento(nome_tipo)
        return {
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "tipo_atendimento": tipo_atendimento,
        }

    def valida_clinica(self):
        # busca a clinica pelo nome digitado; se nao existir, cadastra na hora.
        # Sempre retorna o OBJETO Clinica (nao True), pois o atendimento precisa dele.
        nome_clinica = ler_obrigatorio(self.__view_registro_atendimento.nome_clinica,
                                       self.__view_registro_atendimento.erro_campo_obrigatorio)
        for clinica in self.__sistema_clinicas.clinicas:
            if nome_clinica == clinica.nome:
                return clinica  # clinica ja existia (caminho feliz)
        clinica = self.__cadastrar_clinica_controller.cadastrar(nome_clinica)
        return clinica  # nao existia -> foi cadastrada (caminho triste)

    def valida_paciente(self, clinica):
        # mesmo padrao da clinica: acha o paciente DENTRO da clinica ou cadastra.
        # Retorna o OBJETO Paciente.
        nome_paciente = ler_obrigatorio(self.__view_registro_atendimento.nome_paciente,
                                        self.__view_registro_atendimento.erro_campo_obrigatorio)
        for paciente in clinica.pacientes:
            if nome_paciente == paciente.nome:
                return paciente
        paciente = self.__cadastrar_paciente_controller.cadastrar(clinica, nome_paciente)
        return paciente

    def valida_profissional(self):
        # o profissional precisa JA estar cadastrado (cadastro e via menu, opcao 4).
        # procura pelo nome na lista global; retorna o OBJETO ou None se nao achar.
        nome_profissional = ler_obrigatorio(self.__view_registro_atendimento.nome_profissional,
                                            self.__view_registro_atendimento.erro_campo_obrigatorio)
        for profissional in self.__sistema_clinicas.profissionais:
            if nome_profissional == profissional.nome:
                return profissional
        return None

    def __ler_valor(self):
        # le o valor do atendimento e converte pra float; repete se nao for numero
        while True:
            try:
                return float(self.__view_registro_atendimento.valor())
            except ValueError:
                self.__view_registro_atendimento.erro_valor_invalido()

    def listar(self):
        # LISTAR: todos os atendimentos com dados + valor restante
        linhas = [
            f"{a.paciente.nome} | {a.clinica.nome} | prof: {a.profissional.nome} "
            f"| {a.data} {a.horario_inicio}-{a.horario_fim} | {a.tipo_atendimento.nome} "
            f"| valor: {a.valor} | restante: {a.calcular_valor_restante()}"
            for a in self.__sistema_clinicas.atendimentos
        ]
        self.__view_registro_atendimento.listar_atendimentos(linhas)

    def alterar(self):
        # ALTERAR: escolhe o atendimento e atualiza data, horarios e valor.
        # clinica/paciente/profissional sao vinculos -> ficam fixos.
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        atendimento.data = self.__view_registro_atendimento.data_atendimento()
        atendimento.horario_inicio = self.__view_registro_atendimento.horario_inicio()
        atendimento.horario_fim = self.__view_registro_atendimento.horario_fim()
        atendimento.valor = self.__ler_valor()
        self.__view_registro_atendimento.sucesso_alteracao()

    def excluir(self):
        # EXCLUIR: escolhe o atendimento e remove do sistema
        atendimento = self.__selecionar_atendimento()
        if atendimento is None:
            return
        self.__sistema_clinicas.remover_atendimento(atendimento)
        self.__view_registro_atendimento.sucesso_exclusao()

    def __selecionar_atendimento(self):
        # selecao numerada (atendimento nao tem nome); retorna o objeto ou None
        atendimentos = self.__sistema_clinicas.atendimentos
        if not atendimentos:
            self.__view_registro_atendimento.sem_atendimentos()
            return None
        linhas = [f"{a.paciente.nome} | {a.clinica.nome} | {a.data}" for a in atendimentos]
        escolha = self.__view_registro_atendimento.selecionar_atendimento(linhas)
        if not escolha.isdigit(): # garante que é um digito
            self.__view_registro_atendimento.selecao_invalida()
            return None
        indice = int(escolha) - 1
        if indice < 0 or indice >= len(atendimentos): # garante que o digit não estoura o intervalo da lista atendimentos
            self.__view_registro_atendimento.selecao_invalida()
            return None
        return atendimentos[indice]
