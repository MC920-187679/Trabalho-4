"""
Tratamento de argumentos da linha de comando.
"""
from sys import stdin, stdout
from argparse import ArgumentParser, ArgumentTypeError, FileType
from typing import Tuple, Callable, BinaryIO
from .tipos import Image
from .inout import imgread, imgwrite, imgshow


class Argumentos(ArgumentParser):
    """
    Objeto para tratar opções da linha comando.

    Parâmetros
    ----------
    descricao: str
        Descrição da ferramenta.
    """
    def __init__(self, descricao: str):
        super().__init__(allow_abbrev=False, description=descricao)

        self.add_argument('imagem', metavar='IMAGEM', type=imagem_entrada,
                        help='imagem de entrada')
        self.add_argument('-b', '--bit', type=plano_de_bit, default=0,
                        help='plano de bit')

    def add_saida_imagem(self) -> None:
        """
        Opção para saída de imagens.
        """
        self.add_argument('-o', '--output', dest='saida', type=imagem_saida, default=imgshow,
                        help='salva resultado em arquivo (padrão: exibe em janela)')


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
        img = imgread(arquivo)
        return img, arquivo
    except (OSError, ValueError) as err:
        msg = f"{err}"
        raise ArgumentTypeError(msg) from err

def imagem_saida(arquivo: str) -> Callable[[Image, str], None]:
    """
    Retorna função para codificação e escrita de imagem.
    """
    def saida(img: Image, _entrada: str) -> None:
        imgwrite(img, arquivo)

    return saida


def arquivo_entrada(arquivo: str) -> BinaryIO:
    """
    Abre arquivo binário para leitura.
    """
    if arquivo == '-':
        return stdin.buffer
    else:
        return FileType('rb')(arquivo)

def arquivo_saida(arquivo: str) -> Callable[..., None]:
    """
    Retorna função de escrita em arquivo binário.
    """
    def escreve(*texto: bytes) -> None:
        if arquivo == '-':
            for buf in texto:
                stdout.buffer.write(buf)
        else:
            with open(arquivo, 'wb') as file:
                for buf in texto:
                    file.write(buf)

    return escreve
