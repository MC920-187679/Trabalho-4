"""
Funções de codificação e decodificação para esteganografia.
"""
import numpy as np
from .tipos import Image, Bits


def separa_bits(texto: bytes) -> Bits:
    """
    Separa um string de bytes em um vetor de bits.
    """
    # buffer com o tamanho
    tamanho = len(texto).to_bytes(8, 'big')
    # buffer conjunto
    buffer = np.frombuffer(tamanho + texto, dtype=np.uint8)

    # matriz com cada bit separado
    buf = np.zeros((8, len(buffer)), dtype=np.uint8)
    for i in range(8):
        buf[i] = buffer & 1
        buffer = buffer >> 1

    # vetor de bits
    return buf.T.ravel()

def codifica(img: Image, texto: bytes, bit: int=0) -> Image:
    """
    Codifica arquivo dentro da imagem, no plano de bits especificado.

    Parâmetros
    ----------
    img: ndarray
        Imagem onde arquivo será armazenado.
    texto: bytes
        Vetor de bytes do arquivo.
    bit: int, opcional
        Plano do bit de armazenamento. (padrão = 0)

    Retorno
    -------
    out: ndarray
        Imagem com arquivo codificado.
    """
    # vetor de bits do texto
    buffer = separa_bits(texto)
    tam = len(buffer)
    # cada pixel pode armazenar no máximo um bit
    if tam > img.size:
        imgh, imgw, _ = img.shape
        limite = img.size // 8

        descr = f'imagem {imgh}x{imgw} consegue armazenar no máximo {limite} bytes'
        raise OverflowError(f'{descr}, texto tem {tam // 8} bytes')

    # escrita do texto
    mascara = ~(np.ones(tam, dtype=np.uint8) << bit)
    img.flat[:tam] = (img.flat[:tam] & mascara) | (buffer << bit) # pylint: disable=E1137

    return img


def junta_bits(bits: Bits) -> bytes:
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

def decodifica(img: Image, bit: int=0) -> bytes:
    """

    Parâmetros
    ----------
    img: ndarray
        Imagem onde arquivo foi armazenado.
    bit: int, opcional
        Plano do bit de armazenamento. (padrão = 0)

    Retorno
    -------
    texto: bytes
        Arquivo recuperado.
    """
    # vetor de bits com o texto da imagem
    buffer = ((img >> bit) & 1).flat

    # recupera o tamanho do texto
    tamanho = int.from_bytes(junta_bits(buffer[:64]), 'big')
    # e o texto
    return junta_bits(buffer[64:][:tamanho * 8])
