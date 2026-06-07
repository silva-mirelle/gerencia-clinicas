class ViewCadastrarClinica:
    
    def localizacao(self):
        print("VAMOS CADASTRAR A CLÍNICA - JÁ TEMOS O NOME")
        print("AGORA INDIQUE O RESTO")
        return input("Localização da clinica: ")

    def descricao(self):
        return input("Descrição da clinica: ")

    def listar_clinicas(self, linhas):
        print("---- CLINICAS ----")
        if not linhas:
            print("Nenhuma clinica cadastrada.")
        for linha in linhas:
            print(f"- {linha}")