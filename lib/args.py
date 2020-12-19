from argparse import ArgumentParser, ArgumentTypeError, FileType
from tipos import Image, Literal
from inout import imgread


class Argumentos(ArgumentParser):
    def __init__(self, descricao: str, saida_padrao: str='nova janela'):
        super().__init__(description=descricao)

        self.add_argument('imagem', type=imagem,
                        help='imagem de entrada')
        self.add_argument('-b', '--bit', type=plano_de_bit, default=0,
                        help='plano de bit')
        self.add_argument('-o', '--output', type=str,
                        help=f'saída do resultado (padrão: {saida_padrao})')
        self.add_argument('-f', '--force-show', action='store_true',
                        help='sempre mostra o resultado final na saída padrão')

    def add_texto_entrada(self) -> None:
        self.add_argument('texto', type=FileType('r'),
                        help='texto de entrada')


def plano_de_bit(bit: str) -> int:
    try:
        num = int(bit, base=10)
        if num < 0 or num >= 8:
            raise ArgumentTypeError(f'bit inválido: {bit}')
        return num

    except ValueError as err:
        raise ArgumentTypeError(f'número inválido: {bit}') from err


def imagem(arquivo: str) -> Image:
    try:
        return imgread(FileType('rb')(arquivo))
    except ValueError as err:
        msg = f"problema de leitura da imagem '{arquivo}'"
        raise ArgumentTypeError(msg) from err
