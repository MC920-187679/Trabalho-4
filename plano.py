"""
Ferramenta de extração do plano de bit.
"""
from lib.args import Argumentos
from lib.inout import imgshow, imgwrite


DESCRICAO = 'Ferramenta de extração do plano de bit.'
# parser de argumentos
parser = Argumentos(DESCRICAO)

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # argumentos da cli
    img, arquivo = args.imagem
    bit = args.bit

    # extração do plano do bit
    img = img >> bit
    img = img & 1
    img = 255 * img

    # exibição do resultado
    if args.show or args.output is None:
        # janela
        imgshow(img, arquivo)
    if args.output is not None:
        # arquivo
        imgwrite(img, args.output)
