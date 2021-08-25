from valida_cnpj import digitos, formula
from random import randint


def new_cnpj():
    dig_init = str(randint(10000000, 99999999)) + '0001'
    n_cnpj = dig_init
    if len(n_cnpj) == 12:
        n_cnpj += formula(digitos(dig_init, 1))
    if len(n_cnpj) == 13:
        n_cnpj += formula(digitos(n_cnpj))

    return f'{n_cnpj[:2]}.{n_cnpj[2:5]}.{n_cnpj[5:8]}/{n_cnpj[8:12]}-{n_cnpj[12:14]}'

