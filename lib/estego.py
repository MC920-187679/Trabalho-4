"""
Funções de codificação e decodificação para esteganografia.
"""
import numpy as np
from .tipos import Image
from .permuta import permutacao, despermutacao
from .bits import (
    separa_bytes, separa_int,
    junta_bytes, junta_int,
    cat
)


# # # # # # # #
# CODIFICAÇÃO #

def codifica(img: Image, texto: bytes, bit: int=0, permuta: bool=False) -> Image:
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
    permuta: bool, opcional
        Faz permutação dos dados do arquivo. (padrão = falso)

    Retorno
    -------
    out: ndarray
        Imagem com arquivo codificado.
    """
    # vetor de bit com os dados do arquivo
    dados = separa_bytes(texto)
    if permuta:
        # com permutação, trabalho é feito principalmente
        # na função de permutação
        idx, buffer = permutacao(dados, img.size)
    else:
        # sem permuta, apenas usa primeiros 64 bits para tamanho
        buffer =  cat(separa_int(len(dados)), dados)
        # índices de escrita dos dados
        idx = np.arange(img.size) < len(buffer)

    # indices de acesso na matriz
    idx = idx.reshape(img.shape)
    # primeiro bit (MSB do tamanho) indica se houve permutação
    buffer[0] = int(permuta)

    # checa capacidade
    if len(buffer) > img.size:
        raise OverflowError('arquivo muito grande para a imagem')

    # armazenamento no plano de bit
    mascara = ~(np.ones(len(buffer), dtype=np.uint8) << bit)
    img[idx] = (img[idx] & mascara) | (buffer << bit)

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
    # marcador de permutação
    permutado = bool(buffer[0])
    buffer[0] = 0

    if permutado:
        # despermuta dados
        buffer = despermutacao(buffer)
    else:
        # recupera o tamanho e o texto
        tamanho = junta_int(buffer[:64])
        buffer = buffer[64:][:tamanho]

    # objeto bytes do arquivo
    return junta_bytes(buffer)
