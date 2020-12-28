"""
Operações com vetores de bits.
"""
import numpy as np
from .tipos import Bits


def separa_bytes(texto: bytes) -> Bits:
    """
    Separa um string de bytes em um vetor de bits.
    """
    buffer = np.frombuffer(texto, dtype=np.uint8)

    # matriz com cada bit separado
    buf = np.zeros((8, len(buffer)), dtype=np.uint8)
    for i in range(8):
        buf[i] = (buffer >> i) & 1

    # vetor de bits
    return buf.T.ravel()


def separa_int(num: int, n: int=64) -> Bits:
    """
    Separa um inteiro em um vetor de `n` bits.
    """
    bits = (num >> np.arange(n, dtype=np.uint64)) & 1
    return bits.astype(np.uint8)


def junta_bytes(bits: Bits) -> bytes:
    """
    Junta vetor de bits em uma string de bytes.
    """
    bit = np.reshape(bits, (-1, 8)).T
    # buffer com o resultado
    buf = np.zeros_like(bit[0])
    for i in range(8):
        # junta bit a bit
        buf |= bit[i] << i

    return bytes(buf)


def junta_int(bits: Bits) -> int:
    """
    Junta vetor de bits em um inteiro sem sinal.
    """
    base = (1 << np.arange(len(bits), dtype=np.uint64))
    # print(base, bits, np.sum(bits * base, dtype=np.uint64))
    return int(np.sum(bits * base, dtype=np.uint64))


def cat(*bits: Bits) -> Bits:
    """
    Concatenação de vetores de bits.
    """
    return np.concatenate(bits, axis=None)
