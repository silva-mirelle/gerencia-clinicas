class ViewRegistroAtendimento:

    def nome_clinica(self):
        print("REGISTRO ATENDIMENTO")
        return input("Nome Clinica: ")

    def nome_paciente(self):
        return input("Nome Paciente: ")

    def nome_profissional(self):
        return input("Nome Profissional: ")

    def data_atendimento(self):
        return input("Data do atendimento: ")

    def horario_inicio(self):
        return input("Horario inicio do atendimento: ")

    def horario_fim(self):
        return input("Horario fim do atendimento: ")

    def tipo_atendimento(self):
        return input("Tipo de atendimento: ")

    def valor(self):
        return input("Valor do atendimento: ")

    def aguardando_profissional(self):
        print("Dados do atendimento coletados (clinica, paciente, data, horario, tipo).")
        print("Proximo passo: profissional - aguardando o modulo de cadastro de profissional.")
