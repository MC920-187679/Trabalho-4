"""
Ferramenta de codificação esteganográfica.
"""
from lib.args import Argumentos
from lib.inout import imgshow, imgwrite
from lib.estega import codifica


DESCRICAO = 'Ferramenta de codificação para a técnica de estaganografia.'
# parser de argumentos
parser = Argumentos(DESCRICAO)
parser.add_texto_entrada()

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # argumentos da cli
    img, arquivo = args.imagem
    texto = args.texto.read()

    # codificação
    img = codifica(img, texto, bit=args.bit)

    # exibição do resultado
    if args.force_show or args.output is None:
        # janela
        imgshow(img, arquivo)
    if args.output is not None:
        # arquivo
        imgwrite(img, args.output)
