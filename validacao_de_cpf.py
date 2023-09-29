import re
from os import system, name as OS
from time import sleep


def obter_primeiro_digito(CPF):
    soma = 0
    multiplicador = 10

    for contador in range(len(CPF)):
        soma += int(CPF[contador]) * (multiplicador - contador)
    primeiro_digito = 11 - (soma % 11)

    if primeiro_digito == 10 or primeiro_digito == 11:
        return 0
    else:
        return primeiro_digito


def obter_segundo_digito(CPF):
    soma = 0
    multiplicador = 11

    for contador in range(len(CPF)):
        soma += int(CPF[contador]) * (multiplicador - contador)
    segundo_digito = 11 - (soma % 11)

    if segundo_digito == 10 or segundo_digito == 11:
        return 0
    else:
        return segundo_digito


def cpf_eh_valido(CPF):
    CPF_str = re.sub(r'[-.]', '', CPF)
    resultado = None

    if len(CPF_str) == 11 and CPF_str != '00000000000':
        CPF_str = CPF_str[0:9]

        try:
            primeiro_digito = obter_primeiro_digito(CPF_str)
            CPF_str += ''.join(str(primeiro_digito))

            segundo_digito = obter_segundo_digito(CPF_str)
            CPF_str += ''.join(str(segundo_digito))

            resultado = CPF_str == re.sub(r'[-.]', '', CPF)

        except:
            resultado = None

    return resultado


def cpf_regex(CPF):
    correspondencia = bool(
        re.match(r'^[0-9]{3}\.{0,1}[0-9]{3}\.{0,1}[0-9]{3}\-{0,1}[0-9]{2}$', CPF)
    )
    return correspondencia


def main():
    sistema_operacional = OS

    while True:
        match sistema_operacional:
            case 'nt':
                system('cls')
            case 'posix':
                system('clear')

        print('Seu CPF deve seguir um dos formatos aceitos:\n12345678999 ou 123.456.789-99', end='\n\n')
        CPF = input('Digite o seu CPF: ')

        if cpf_regex(CPF) and cpf_eh_valido(CPF):
            print(f'\nCPF válido!')
            break

        elif not cpf_eh_valido(CPF):
            print('\nO CPF não é válido!')

        elif not cpf_regex(CPF):
            print('\nO CPF informado não segue o padrão solicidato!')

        print('Revise os dados digitados e tente novamente.')

        sleep(2.75)


if __name__ == '__main__':
    main()
