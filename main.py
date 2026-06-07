# Ponto de entrada (entry point) da aplicacao.
# Unico arquivo que se RODA diretamente (python main.py). Ele apenas monta o
# controlador principal e da o "start"; nao contem regra de negocio nem tela.
from iniciar_controller import IniciarController


def main():
    # cria o maestro (IniciarController) e entrega o controle pra ele
    controller = IniciarController()
    controller.iniciar_atendimento()


# So executa main() quando ESTE arquivo e o rodado diretamente
# (se for importado por outro modulo, __name__ != "__main__" e nada roda).
if __name__ == "__main__":
    main()
