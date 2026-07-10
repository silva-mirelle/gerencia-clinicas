# "Banco de dados" do sistema (registro central).
# Todas as colecoes de topo sao persistidas via DAO (serializacao em disco).
# Paciente (dentro da clinica), procedimento e pagamento (dentro do atendimento)
# sao persistidos junto do seu dono. Uma unica instancia e compartilhada por
# todos os controllers (criada no IniciarController).
from daos.clinica_dao import ClinicaDAO
from daos.tipo_atendimento_dao import TipoAtendimentoDAO
from daos.profissional_saude_dao import ProfissionalSaudeDAO
from daos.atendimento_dao import AtendimentoDAO


class SistemaClinicas:
    def __init__(self):
        self.__clinica_dao = ClinicaDAO()               # clinicas.pkl
        self.__tipo_atendimento_dao = TipoAtendimentoDAO()  # tipos_atendimento.pkl
        self.__profissional_dao = ProfissionalSaudeDAO()    # profissionais.pkl
        self.__atendimento_dao = AtendimentoDAO()           # atendimentos.pkl

    @property
    def clinicas(self):
        # expoe como lista (os controllers iteram/indexam por lista)
        return list(self.__clinica_dao.get_all())

    def registrar_clinica(self, clinica):
        # o DAO atribui o codigo sequencial e persiste
        self.__clinica_dao.add(clinica)
        print("----CLINICA REGISTRADA COM SUCESSO----")

    def remover_clinica(self, clinica):
        self.__clinica_dao.remove(clinica.codigo)

    def atualizar_clinica(self, clinica):
        # re-persiste a clinica apos alteracao em memoria (add com codigo ja
        # existente sobrescreve a mesma chave e regrava o arquivo)
        self.__clinica_dao.add(clinica)

    @property
    def tipos_atendimento(self):
        return list(self.__tipo_atendimento_dao.get_all())

    def registrar_tipo_atendimento(self, tipo):
        self.__tipo_atendimento_dao.add(tipo)  # DAO atribui codigo e persiste
        print("----TIPO DE ATENDIMENTO REGISTRADO COM SUCESSO----")

    def remover_tipo_atendimento(self, tipo):
        self.__tipo_atendimento_dao.remove(tipo.codigo)

    def atualizar_tipo_atendimento(self, tipo):
        # re-persiste apos alteracao (add com codigo existente sobrescreve)
        self.__tipo_atendimento_dao.add(tipo)

    @property
    def profissionais(self):
        return list(self.__profissional_dao.get_all())

    def registrar_profissional(self, profissional):
        self.__profissional_dao.add(profissional)  # indexado por cpf
        print("----PROFISSIONAL REGISTRADO COM SUCESSO----")

    def remover_profissional(self, profissional):
        self.__profissional_dao.remove(profissional.cpf)

    def atualizar_profissional(self, profissional):
        self.__profissional_dao.add(profissional)

    @property
    def atendimentos(self):
        return list(self.__atendimento_dao.get_all())

    def registrar_atendimento(self, atendimento):
        self.__atendimento_dao.add(atendimento)  # DAO atribui codigo e persiste

    def remover_atendimento(self, atendimento):
        self.__atendimento_dao.remove(atendimento.codigo)

    def atualizar_atendimento(self, atendimento):
        # re-persiste o atendimento (usado quando procedimentos/pagamentos internos
        # mudam, ou quando os dados do proprio atendimento sao alterados)
        self.__atendimento_dao.add(atendimento)

    # ---- RELATORIOS (so computacao sobre os dados; quem exibe e o controller/view) ----

    def procedimentos_mais_realizados(self):
        # conta os procedimentos por descricao em TODOS os atendimentos.
        # retorna lista de (descricao, quantidade), da mais realizada pra menos.
        contagem = {}
        for atendimento in self.atendimentos:
            for procedimento in atendimento.procedimentos:
                contagem[procedimento.descricao] = contagem.get(procedimento.descricao, 0) + 1
        return sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    def procedimentos_por_custo(self):
        # junta os procedimentos de todos os atendimentos e ordena por custo (crescente).
        # o controller usa o primeiro (mais barato) e o ultimo (mais caro).
        procedimentos = [p for a in self.atendimentos for p in a.procedimentos]
        return sorted(procedimentos, key=lambda p: p.custo)

    def clinicas_por_numero_atendimentos(self):
        # conta quantos atendimentos cada clinica tem (via atendimento.clinica).
        # retorna lista de (nome_clinica, quantidade), da que tem mais pra menos.
        contagem = {}
        for atendimento in self.atendimentos:
            nome = atendimento.clinica.nome
            contagem[nome] = contagem.get(nome, 0) + 1
        return sorted(contagem.items(), key=lambda item: item[1], reverse=True)

    def atendimentos_por_valor(self):
        # atendimentos ordenados por valor (crescente).
        # o controller usa o primeiro (mais barato) e o ultimo (mais caro).
        return sorted(self.atendimentos, key=lambda a: a.valor)
