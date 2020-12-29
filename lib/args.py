"""
Tratamento de argumentos da linha de comando.
"""
from sys import stdin, stdout
from warnings import warn
from argparse import (
    ArgumentParser, FileType,
    ArgumentTypeError, Namespace
)
from typing import (
    Tuple, Callable, BinaryIO,
    Optional, Sequence
)
from .tipos import Image
from .inout import encode, decode, imgshow, imgwrite


class Argumentos(ArgumentParser):
    """
    Objeto para tratar opções da linha comando.

    Parâmetros
    ----------
    descricao: str
        Descrição da ferramenta.
    """
    def __init__(self, descricao: str, add_imagem: bool=True):
        super().__init__(allow_abbrev=False, description=descricao)

        if add_imagem:
            self.add_entrada_imagem('imagem')

    def add_plano_de_bit(self) -> None:
        """
        Opção para plano de bits.
        """
        self.add_argument('-b', '--bit', type=plano_de_bit, default=0,
                        help='plano de bit (padrão: 0)')

    def add_entrada_imagem(self, var: str, descricao: str='imagem de entrada') -> None:
        """
        Opção para entrada de imagens.
        """
        self.add_argument(var, metavar=var.upper(), type=imagem_entrada, help=descricao)

    def add_saida_imagem(self) -> None:
        """
        Opção para saída de imagens.
        """
        self.add_argument('-o', '--output', dest='saida', type=imagem_saida, default=imgshow,
                        help='salva resultado em arquivo (padrão: exibe em janela)')

    def parse_intermixed_args(self, args: Optional[Sequence[str]]=None,
                              namespace: Optional[Namespace]=None) -> Namespace:
        """
        Parser de argumentos com ordem mistas.
        Só funciona em Python 3.7 ou superior.
        """
        try:
            return super().parse_intermixed_args(args, namespace)
        except AttributeError:
            warn('Python 3.6 não suporta argumentos opcionais após entrada')
            return super().parse_args(args, namespace)


def plano_de_bit(bit: str) -> int:
    """
    Leitura de argumento de plano de bit válido (0-7).
    """
    try:
        num = int(bit, base=10)
        if num < 0 or num >= 8:
            raise ArgumentTypeError('fora do intervalo [0-7]')
        return num

    except ValueError as err:
        raise ArgumentTypeError(f'número inválido: {bit}') from err


def imagem_entrada(arquivo: str) -> Tuple[Image, str]:
    """
    Leitura e decodificação de imagem.
    """
    try:
        # argumento especial
        if arquivo == '-':
            return decode(stdin.buffer.read()), '[STDIN]'
        # arquivos comuns
        with open(arquivo, 'rb') as file:
            return decode(file.read()), arquivo

    except (OSError, ValueError) as err:
        raise ArgumentTypeError(str(err)) from err

def imagem_saida(arquivo: str) -> Callable[[Image, str], None]:
    """
    Retorna função para codificação e escrita de imagem.
    """
    def saida(img: Image, _entrada: str) -> None:
        # argumento especial
        if arquivo == '-':
            stdout.buffer.write(encode(img))
        # arquivos comuns
        else:
            imgwrite(img, arquivo)

    return saida


def arquivo_entrada(arquivo: str) -> BinaryIO:
    """
    Abre arquivo binário para leitura.
    """
    # argumento especial
    if arquivo == '-':
        return stdin.buffer

    return FileType('rb')(arquivo)

def arquivo_saida(arquivo: str) -> Callable[..., None]:
    """
    Retorna função de escrita em arquivo binário.
    """
    def escreve(*texto: bytes) -> None:
        # argumento especial
        if arquivo == '-':
            for buf in texto:
                stdout.buffer.write(buf)
        else:
            # arquivos comuns
            with open(arquivo, 'wb') as file:
                for buf in texto:
                    file.write(buf)

    return escreve
