import re
from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome_informado):
    return nome_informado.isalpha()

def rg_valido(rg_informado):
    return len(rg_informado) == 9

def celular_valido(celular_informado):
    """Verifica se o celular tem o padrão '99 99999-9999' """
    pattern = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resp = re.findall(pattern, celular_informado)
    return resp
