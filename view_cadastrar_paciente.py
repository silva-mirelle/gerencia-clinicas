class ViewCadastrarPaciente:
    
    def celular(self):
        print("VAMOS CADASTRAR O PACIENTE - JÁ TEMOS O NOME")
        print("---- AGORA INDIQUE ----")
        return input("Celular (somente numeros): ")

    def cpf(self):
        return input("CPF (somente numeros): ")

    def data_nascimento(self):
        return input("Data de nascimento (somente numeros): ")

    def erro_apenas_numeros(self):
        print("Entrada invalida: use apenas numeros (0-9), sem espacos, letras ou simbolos.")

    def listar_pacientes(self, linhas):
        print("---- PACIENTES ----")
        if not linhas:
            print("Nenhum paciente cadastrado.")
        for linha in linhas:
            print(f"- {linha}")