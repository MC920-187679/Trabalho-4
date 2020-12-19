"""
Ferramenta de extração do plano de bit.
"""
from argparse import ArgumentTypeError
from lib.args import Argumentos
from lib.inout import imgshow, imgwrite


# canais válidos
CORES = ['B', 'G', 'R']

def canal_de_cor(cor: str) -> int:
    """
    Leitura de canal de cor.
    """
    try:
        return CORES.index(cor)
    except ValueError as err:
        msg = 'canal de cor inválido'
        raise ArgumentTypeError(msg) from err


# parser de argumentos
parser = Argumentos('Ferramenta de extração do plano de bit.')
parser.add_argument('-i', '--inverte', action='store_true',
                    help='inverte resultado')
# opções de extração de canal de cores
parser.add_argument('-c', '--cor', choices=CORES, type=canal_de_cor,
                    help='extração de um canal de cor (padrão: todos)')
parser.add_argument('-d', '--fundo-branco', dest='fundo',
                    action='store_const', default=0, const=255,
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
        # para imagem colorida
        else:
            outros = [c for c in CORES if c != args.cor]
            img[..., outros] = args.fundo

    # exibição do resultado
    if args.show or args.output is None:
        # janela
        imgshow(img, arquivo)
    if args.output is not None:
        # arquivo
        imgwrite(img, args.output)
