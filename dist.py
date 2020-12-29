"""
Medição de similaridade entre imagens.
"""
import numpy as np
from lib.args import Argumentos


def EMAX(f, g):
    return np.max(np.abs(f - g))

def MAE(f, g):
    return np.mean(np.abs(f - g))

def MSE(f, g):
    return np.mean(np.square(f - g))

def RMSE(f, g):
    return np.sqrt(MSE(f, g))

def NMSE(f, g):
    return MSE(f, g) / MSE(f, 0)

def PSNR(f, g, Lmax=255):
    return 20 * np.log10(Lmax / RMSE(f, g))

def SNR(f, g):
    return 20 * np.log10(MSE(f, 0) / MSE(f, g))

def cov(f, g):
    return np.cov(f.flat, g.flat)[0,1]

def corr(f, g):
    cov = np.cov(f.flat, g.flat)
    vf, vg = np.diag(cov)
    return cov[0,1] / np.sqrt(vf * vg)

def jaccard(f, g):
    return np.mean(f == g)

# todos as medidas acima
METODOS = {
    'EMAX': EMAX, 'MAE': MAE, 'RMSE': RMSE,
    'PSNR': PSNR, 'SNR': SNR, 'COV': cov,
    'COR': corr, 'JACC': jaccard
}

# parser dos argumentos da linha de comando
parser = Argumentos('Medida de similaridade entre imagens.', add_imagem=False)
parser.add_entrada_imagem('img1')
parser.add_entrada_imagem('img2')
parser.add_argument('medida', metavar='MEDIDA', nargs='*', default=METODOS.keys())
parser.add_argument('-b', '--bit', type=int, default=None)


if __name__ == '__main__':
    args = parser.parse_intermixed_args()

    (f, _), (g, _) = args.img1, args.img2
    # extração do bit escolhido
    if args.bit is not None:
        f = (f >> args.bit) & 1
        g = (g >> args.bit) & 1
        # a imagem agora é apenas 1 nível de cinza
        METODOS['PSNR'] = lambda f, g: PSNR(f, g, Lmax=1)
    # ponto flutuante para evitar arredondamentos
    f = f.astype(np.float64)
    g = g.astype(np.float64)

    # com apenas uma medida, não mostra nome
    if len(args.medida) == 1:
        metodo = args.medida.pop()
        dist = METODOS[metodo.upper()](f, g)
        print(dist)
    # com mais de uma, sim
    for metodo in args.medida:
        dist = METODOS[metodo.upper()](f.copy(), g.copy())
        print(dist, metodo)
