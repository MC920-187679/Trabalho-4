"""
Ferramenta de decodificação do arquivo codificado por 'codificar.py'.
"""
from lib.args import Argumentos, arquivo_saida
from lib.estego import decodifica


DESCRICAO = 'Ferramenta de decodificação de arquivo em imagem.'
# parser de argumentos
parser = Argumentos(DESCRICAO)
parser.add_plano_de_bit()
# opções de saída
parser.add_argument('saida', metavar='SAIDA', type=arquivo_saida, default='-', nargs='?',
                    help='arquivo para armazenar resultado')
parser.add_argument('-n', dest='end', action='store_const', const=b'\n', default=b'',
                    help='imprime nova linha no final')

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # imagem pela cli
    img, _ = args.imagem

    # decodificação
    texto = decodifica(img, bit=args.bit)

    # exibição do resultado
    args.saida(texto, args.end)
