"""
Tratamento de argumentos da linha de comando.
"""
from argparse import ArgumentParser, ArgumentTypeError
from typing import Tuple, Optional
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
        self.add_argument('-b', '--bit', type=Numero(8), default=0,
                        help='plano de bit')
        self.add_argument('-o', '--output', type=str,
                        help=f'saída do resultado (padrão: {saida_padrao})')
        self.add_argument('-f', '--force-show', action='store_true', dest='show',
                        help='sempre mostra o resultado final na saída padrão')


def imagem(arquivo: str) -> Tuple[Image, str]:
    """
    Leitura e decodificação de imagem.
    """
    try:
        img = imgread(arquivo)
        return img, arquivo
    # erro de leitura ou de decodificação
    except (OSError, ValueError) as err:
        msg = f"{err}"
        raise ArgumentTypeError(msg) from err


class Numero:
    """
    Leitura de inteiro dentro de um range.
    Parâmetros similares a um `range`.
    """
    def __init__(self, start: int, stop: Optional[int]=None):
        if stop is None:
            start, stop = 0, start

        self.range = range(start, stop)

    def parse(self, num: str) -> int:
        """
        Parser de um número e verificação do range.
        """
        ans = int(num, base=10)
        # número fora do intervalo
        if ans not in self.range:
            i, j = self.range.start, self.range.stop - 1
            msg = f'número fora do intervalo [{i}, {j}]'
            raise OverflowError(msg)

        return ans


    def __call__(self, num: str) -> int:
        """
        Chamada para tratamento de argumentos.
        """
        try:
            return self.parse(num)
        # inteiro inválido ou fora do range
        except (ValueError, OverflowError) as err:
            raise ArgumentTypeError(f'{err}') from err
