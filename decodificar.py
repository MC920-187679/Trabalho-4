"""
Ferramenta de decodificação do arquivo codificado por 'codificar.py'.
"""
from argparse import FileType
from lib.args import Argumentos
from lib.estega import decodifica


DESCRICAO = 'Ferramenta de decodificação de arquivo em imagem.'
# parser de argumentos
parser = Argumentos(DESCRICAO)
parser.add_argument('saida', metavar='SAIDA', type=FileType('wb'),
                    help='arquivo para armazenar resultado')
parser.add_argument('-n', dest='end', action='store_const', const=b'\n', default=b'',
                    help='imprime nova linha')

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # imagem pela cli
    img, _ = args.imagem

    # decodificação
    texto = decodifica(img, bit=args.bit)

    # exibição do resultado
    args.saida.write(texto)
    args.saida.write(args.end)
