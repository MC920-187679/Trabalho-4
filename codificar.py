"""
Ferramenta de codificação esteganográfica.
"""
from lib.args import Argumentos, arquivo_entrada
from lib.estego import codifica


DESCRICAO = 'Ferramenta de codificação para a técnica de estaganografia.'
# parser de argumentos
parser = Argumentos(DESCRICAO)
parser.add_saida_imagem()
# arquivo a ser codificado
parser.add_argument('arquivo', metavar='ARQUIVO', type=arquivo_entrada, default='-', nargs='?',
                    help='arquivo de entrada')


if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # argumentos da cli
    img, arquivo = args.imagem
    texto = args.arquivo.read()

    # codificação
    img = codifica(img, texto, bit=args.bit)

    # exibição do resultado
    args.saida(img, arquivo)
