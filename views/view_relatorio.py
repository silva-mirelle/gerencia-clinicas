# VIEW (Tela) dos relatorios (MVC). So exibe; recebe titulo + linhas prontas.
class ViewRelatorio:

    def mostrar_relatorio(self, titulo, linhas):
        print(f"---- RELATORIO: {titulo} ----")
        if not linhas:
            print("Sem dados para este relatorio.")
        for linha in linhas:
            print(f"- {linha}")
