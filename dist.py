"""
Medição de similaridade entre imagens.
"""
import sys, cv2
import numpy as np


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

METODOS = {
    'EMAX': EMAX, 'MAE': MAE, 'RMSE': RMSE,
    'PSNR': PSNR, 'SNR': SNR, 'COV': cov,
    'COR': corr, 'JACC': jaccard
}

try:
    _, f, g, metodo = sys.argv
except ValueError:
    _, f, g = sys.argv
    metodo = METODOS.keys()

f = cv2.imread(f, cv2.IMREAD_COLOR)
g = cv2.imread(g, cv2.IMREAD_COLOR)
assert f is not None and g is not None
f, g = f.astype(np.float64), g.astype(np.float64)


if isinstance(metodo, str):
    dist = METODOS[metodo.upper()](f, g)
    print(dist)

for mtd in metodo:
    dist = METODOS[mtd](f.copy(), g.copy())
    print(dist, mtd)
