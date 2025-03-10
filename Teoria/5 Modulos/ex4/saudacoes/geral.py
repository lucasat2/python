def saudar(nome, tipo):
    if tipo == "formal":
        from .formal import cumprimentar
    elif tipo == "informal":
        from .informal import cumprimentar
    else:
        raise ValueError("Tipo de saudação desconhecido. Use 'formal' ou 'informal'.")
    cumprimentar(nome)
