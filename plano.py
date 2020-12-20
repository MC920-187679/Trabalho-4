"""
Ferramenta de extração do plano de bit.
"""
from argparse import ArgumentTypeError
from enum import IntEnum, unique
from lib.args import Argumentos
from lib.inout import imgshow, imgwrite


@unique
class Cor(IntEnum):
    """
    Canais de cores válidos na imagem.
    """
    B = 0
    G = 1
    R = 2

    @classmethod
    def parse(cls, cor: str) -> 'Cor':
        """
        Leitura de canal de cor.
        """
        try:
            return cls[cor]
        except ValueError as err:
            msg = 'canal de cor inválido'
            raise ArgumentTypeError(msg) from err

    def __str__(self) -> str:
        return str(self.name)


# parser de argumentos
parser = Argumentos('Ferramenta de extração do plano de bit.')
parser.add_argument('-i', '--inverte', action='store_true',
                    help='inverte resultado')
# opções de extração de canal de cores
parser.add_argument('-c', '--cor', choices=Cor, type=Cor.parse,
                    help='extração de um canal de cor (padrão: todos)')
parser.add_argument('-d', '--fundo-branco', action='store_true',
                    help='extração de canal em fundo branco (padrão: preto)')
parser.add_argument('-g', '--grayscale', action='store_true',
                    help='extração de canal de cor em escala de cinza')


if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # argumentos da cli
    img, arquivo = args.imagem
    bit = args.bit

    # extração do plano do bit
    img = img >> bit
    img = img & 1
    img = 255 * img

    # inversão do resultado
    if args.inverte:
        img = ~img

    # extração de um canal de cor
    if args.cor is not None:
        # para escala de cinza
        if args.grayscale:
            img = img[..., args.cor]
        # para imagem colorida com fundo preto
        elif not args.fundo_branco:
            idx = [c for c in Cor if c != args.cor]
            img[..., idx] = 0
        # e com fundo branco
        else:
            for c in Cor:
                if c == args.cor:
                    continue
                img[..., c] = ~img[..., args.cor]
            img[..., args.cor] = 255

    # exibição do resultado
    if args.show or args.output is None:
        # janela
        imgshow(img, arquivo)
    if args.output is not None:
        # arquivo
        imgwrite(img, args.output)
