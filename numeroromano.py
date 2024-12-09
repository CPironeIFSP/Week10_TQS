def converte(numeroEmRomano):
    """
    Converte um número romano para um número inteiro.
    :param numeroEmRomano: (str) Número romano.
    :return: (int) Número inteiro correspondente.
    """
    tabela = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not numeroEmRomano:
        raise ValueError("O número romano não pode estar vazio.")

    # Validação: Verifica se todos os caracteres são válidos
    if not all(c in tabela for c in numeroEmRomano):
        raise ValueError("O número romano contém caracteres inválidos.")

    acumulador = 0
    ultimovizinhodireita = 0

    for letra in reversed(numeroEmRomano):
        valor_atual = tabela[letra]

        # Adiciona ou subtrai conforme a regra
        if valor_atual < ultimovizinhodireita:
            acumulador -= valor_atual
        else:
            acumulador += valor_atual

        ultimovizinhodireita = valor_atual

    return acumulador
