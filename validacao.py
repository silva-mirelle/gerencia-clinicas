# Funcao utilitaria de validacao de entrada, reutilizada pelos controllers (DRY).
# Mantem a regra "campo obrigatorio" num lugar so.
def ler_obrigatorio(metodo_view, metodo_erro):
    # repete ate o usuario digitar algo nao-vazio (ignora espacos nas pontas).
    # metodo_view: funcao da tela que LE o campo; metodo_erro: funcao da tela que AVISA.
    valor = metodo_view().strip()
    while valor == "":
        metodo_erro()
        valor = metodo_view().strip()
    return valor
