import re


def formata_cpf(cpf):  # Formatação texto
    return re.sub(r'[^0-9]', '', cpf)


def digitos(value_cnpj, chave=0):
    base = list(range(6, 1, -1)) + list(range(9, 1, -1))  # [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    return sum([x * int(y) for x, y in zip(base[chave:], value_cnpj)])


def formula(soma_digitos):
    result = 11 - (soma_digitos % 11)
    if result > 9:
        return '0'
    else:
        return str(result)


def novo_cnpj_re(cnpj, cnpj_str):
    if not cnpj or len(cnpj) < 14:
        return False
    else:
        if len(cnpj_str) == 12:
            cnpj_str += formula(digitos(cnpj, 1))
        if len(cnpj_str) == 13:
            cnpj_str += formula(digitos(cnpj_str))
        return cnpj_str == cnpj
