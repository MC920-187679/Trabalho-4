"""
Ferramenta de decodificação do texto codificado por 'codificar.py'.
"""
from lib.args import Argumentos
from lib.estega import decodifica


DESCRICAO = 'Ferramenta de decodificação de texto em imagem.'
# parser de argumentos
parser = Argumentos(DESCRICAO, saida_padrao='stdout')

if __name__ == '__main__':
    args = parser.parse_intermixed_args()
    # imagem pela cli
    img, _ = args.imagem

    # decodificação
    texto = decodifica(img, bit=args.bit)

    # exibição do resultado
    if args.force_show or args.output is None:
        # stdout
        print(texto)
    if args.output is not None:
        # arquivo de saída
        with open(args.output, 'w') as arquivo:
            print(texto, file=arquivo)
