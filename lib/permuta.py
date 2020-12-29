"""
Permutação dos dados do arquivo.
"""
from typing import Optional, Tuple
import numpy as np
from numpy.random import Generator
from .tipos import Bits, Indices
from .bits import separa_int, junta_int, cat


def rng(chave: Optional[int]=None) -> Generator:
    """
    Random Number Generator do Numpy.
    """
    return np.random.default_rng(chave)


# # # # # # # #
# CODIFICAÇÃO #

# Largura dos inteiros utilizados
INTW = 64

def gera_chave() -> int:
    """
    Gera nova chave de permutação.
    """
    # chave gerada por 8 bytes aleatorios
    dados = rng().bytes(INTW // 8)
    # chave também separada em bits
    return int.from_bytes(dados, 'little')


def permutacao(buffer: Bits, cap: int) -> Tuple[Indices, Bits]:
    """
    Permutação do buffer com os dados do arquivo,
    tentando distribuir os dados em toda a capacidade
    da imagem.

    Parâmetros
    ----------
    buffer: ndarray
        Dados do arquivo.
    cap: int
        Capacidade de armazenamento da imagem, ou
        quantidade de bytes na pixel. Deve ser
        maior ou igual a `len(buffer) + 128`.

    Retorno
    -------
    idx: ndarray
        Índices pseudo-aleatórios para inserção dos
        dados do arquivo.
    bits: ndarray
        Vetor de bits com os dados do arquivo
        reordenados e com cabeçalho (tamanho)
        e rodapé (chave de permutação).
    """
    # sempre cria chave nova aleatória
    chave = gera_chave()
    # para semear as permutações
    rand = rng(chave)
    # rodapé: chave usada
    ch_bits = separa_int(chave, INTW)

    tam = len(buffer)
    # cabeçalho: tamanho do buffer
    tam_bits = separa_int(tam, INTW)

    p = rand.permutation(tam)
    # junta o cabeçalho, os dados permutados e o rodapé
    buffer = cat(tam_bits, buffer[p], ch_bits)

    idx = np.zeros(cap - 2 * INTW, dtype=np.bool)
    # indice das posições de dados (sem cabeçalho nem rodapé)
    idx[:tam] = True
    # embaralhados também
    rand.shuffle(idx)

    idx_tam = np.ones(INTW, dtype=np.bool)
    # índices de inserção dos dados em 'buffer'
    idx = cat(idx_tam, idx, idx_tam)

    return idx, buffer


# # # # # # # # #
# DECODIFICAÇÃO #

def invp(p: np.ndarray) -> np.ndarray:
    """
    Encontra a permutação inversa de `p`.
    """
    inv = np.zeros_like(p)
    inv[p] = np.arange(len(p), dtype=p.dtype)
    return inv


def despermutacao(buffer: Bits) -> Bits:
    """
    Desfaz a permutação no buffer.

    Parâmetros
    ----------
    buffer: ndarray
        Dados permutados, com cabeçalho e rodapé.

    Retorno
    -------
    out: ndarray
        Dados recuperados.
    """
    # leitura do tamanho (no cabeçalho)
    tam = junta_int(buffer[:INTW])
    # e da chave (no rodapé)
    rand = rng(junta_int(buffer[-INTW:]))

    # permutação inversa da usada
    p = invp(rand.permutation(tam))

    idx = np.zeros(len(buffer) - 2 * INTW, dtype=np.bool)
    idx[:tam] = True
    # mesmo vetor dos indices de inserção
    rand.shuffle(idx)

    # acesso reverso
    return buffer[INTW:-INTW][idx][p]
