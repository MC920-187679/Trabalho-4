"""
Ferramenta de decodificação do texto codificado por 'codificar.py'.
"""
from sys import stdout
from lib.args import Argumentos
from lib.estega import decodifica


DESCRICAO = 'Ferramenta de decodificação de texto em imagem.'
# parser de argumentos
parser = Argumentos(DESCRICAO, saida_padrao='stdout')
parser.add_argument('-n', dest='end', action='store_const', const='\n', default='',
                    help='imprime nova linha')

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # imagem pela cli
    img, _ = args.imagem

    # decodificação
    texto = decodifica(img, bit=args.bit)

    # exibição do resultado
    if args.show or args.output is None:
        # stdout
        stdout.write(texto)
        stdout.write(args.end)
    if args.output is not None:
        # arquivo de saída
        with open(args.output, 'w') as arquivo:
            arquivo.write(texto)
            arquivo.write(args.end)
