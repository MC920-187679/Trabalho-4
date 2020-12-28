"""
Funções de codificação e decodificação para esteganografia.
"""
import numpy as np
from .tipos import Image
from .bits import (
    separa_bytes, separa_int,
    junta_bytes, junta_int,
    cat
)


# # # # # # # #
# CODIFICAÇÃO #

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
    # vetor de bits do arquivo, com os primeiros 64 bits indicando tamanho
    buffer = cat(separa_int(len(texto)), separa_bytes(texto))
    # checa capacidade
    tam = len(buffer)
    if tam > img.size:
        raise OverflowError('arquivo muito grande para a imagem')

    # armazenamento no plano de bit
    mascara = ~(np.ones(tam, dtype=np.uint8) << bit)
    img.flat[:tam] = (img.flat[:tam] & mascara) | (buffer << bit) # pylint: disable=E1137

    return img


# # # # # # # # #
# DECODIFICAÇÃO #

def decodifica(img: Image, bit: int=0) -> bytes:
    """
    Decodifica arquivo armazenado na imagem.

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
    # buffer com o plano de bit
    buffer = ((img >> bit) & 1).ravel('C')

    # recupera o tamanho do texto
    tamanho = junta_int(buffer[:64])
    # e o texto
    return junta_bytes(buffer[64:][:tamanho * 8])
