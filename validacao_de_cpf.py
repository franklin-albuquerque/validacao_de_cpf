import re
from os import system, name as sistema_operacional
from time import sleep


class ValidacaoDeCPF:
    def __init__(self, cpf):
        self.cpf = re.sub(r'[.-]', '', cpf)
        self.cpf_entrada = cpf


    def obter_primeiro_digito(self, cpf):
        total = 0
        multiplicador = 10

        for contador in range(len(cpf)):
            total += int(cpf[contador]) * (multiplicador - contador)
        primeiro_digito = 11 - (total % 11)

        if primeiro_digito not in (10, 11):
            return primeiro_digito
        else:
            return 0


    def obter_segundo_digito(self, cpf):
        total = 0
        multiplicador = 11

        for contador in range(len(cpf)):
            total += int(cpf[contador]) * (multiplicador - contador)
        segundo_digito = 11 - (total % 11)

        if segundo_digito not in (10, 11):
            return segundo_digito
        else:
            return 0


    def cpf_eh_valido(self):
        resultado = None

        if len(self.cpf) == 11 and self.cpf != self.cpf[0]*11:
            validacao = ValidacaoDeCPF(self.cpf)
            self.cpf = self.cpf[0:9]

            try:
                self.cpf += ''.join(str(validacao.obter_primeiro_digito(self.cpf)))
                self.cpf += ''.join(str(validacao.obter_segundo_digito(self.cpf)))
                resultado = (self.cpf == re.sub(r'[.-]', '', self.cpf_entrada))
            except Exception:
                resultado = None

        return resultado


    def expressao_regular(self):
        return bool(
            re.match(r'(^[0-9]{11}$|^[0-9]{3}\.{1}[0-9]{3}\.{1}[0-9]{3}\-{1}[0-9]{2}$)', self.cpf_entrada)
        )


def main():
    while True:
        [system('cls') if sistema_operacional == 'nt' else system('clear')]

        print('O seu CPF deve estar em um dos formatos aceitos:\n123.456.789-99 ou 12345678999', end='\n\n')
        cpf = input('Digite o seu CPF: ')

        validacao = ValidacaoDeCPF(cpf)

        if not validacao.cpf_eh_valido():
            print('\nO CPF fornecido é inválido!')
        elif not validacao.expressao_regular():
            print('\nO CPF fornecido não está em nenhum dos formatos aceitos.')
        else:
            print(f'\nO CPF fornecido é válido!')
            break

        print('Por favor, verifique os dados inseridos e tente novamente.')
        sleep(3.25)


if __name__ == '__main__':
    main()
