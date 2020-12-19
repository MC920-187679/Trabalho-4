"""
Tratamento de argumentos da linha de comando.
"""
from argparse import ArgumentParser, ArgumentTypeError, FileType
from typing import Tuple
from .tipos import Image
from .inout import imgread


class Argumentos(ArgumentParser):
    """
    Objeto para tratar opções da linha comando.

    Parâmetros
    ----------
    descricao: str
        Descrição da ferramenta.
    saida_padrao: str, opcional
        Descrição da saída usada por padrão na ferramenta.
    """
    def __init__(self, descricao: str, saida_padrao: str='nova janela'):
        super().__init__(allow_abbrev=False, description=descricao)

        self.add_argument('imagem', metavar='IMAGEM', type=imagem,
                        help='imagem de entrada')
        self.add_argument('-b', '--bit', type=plano_de_bit, default=0,
                        help='plano de bit')
        self.add_argument('-o', '--output', type=str,
                        help=f'saída do resultado (padrão: {saida_padrao})')
        self.add_argument('-f', '--force-show', action='store_true',
                        help='sempre mostra o resultado final na saída padrão')

    def add_texto_entrada(self) -> None:
        """
        Adiciona texto como entrada opcional.
        """
        self.add_argument('texto', metavar='TEXTO', type=FileType('r'), default='-', nargs='?',
                        help='texto de entrada')


def plano_de_bit(bit: str) -> int:
    """
    Leitura de argumento de plano de bit válido (0-7).
    """
    try:
        num = int(bit, base=10)
        if num < 0 or num >= 8:
            raise ArgumentTypeError(f'bit inválido: {bit}')
        return num

    except ValueError as err:
        raise ArgumentTypeError(f'número inválido: {bit}') from err


def imagem(arquivo: str) -> Tuple[Image, str]:
    """
    Leitura e decodificação de imagem.
    """
    try:
        img = imgread(arquivo)
        return img, arquivo
    except (OSError, ValueError) as err:
        msg = f"{err}"
        raise ArgumentTypeError(msg) from err
