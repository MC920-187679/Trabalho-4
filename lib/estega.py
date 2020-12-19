"""
Funções de codificação e decodificação para esteganografia.
"""
from tipos import Image, Bits
import numpy as np


def separa_bits(texto: str) -> Bits:
    """
    Separa uma string em um vetor de bits, codificado em 'utf8'.
    """
    # buffer de bytes com o texto
    texto_buf =  texto.encode('utf8')
    # buffer com o tamanho
    tamanho = len(texto_buf).to_bytes(8, 'big')
    # buffer conjunto
    buffer = np.frombuffer(tamanho + texto_buf, dtype=np.uint8)

    # matriz com cada bit separado
    buf = np.zeros((8, len(buffer)), dtype=np.uint8)
    for i in range(8):
        buf[i] = buffer & 1
        buffer = buffer >> 1

    # vetor de bits
    return buf.T.ravel()

def codifica(img: Image, texto: str, bit: int=0) -> Image:
    """
    Codifica texto dentro da imagem, no plano de bits especificado.

    Parâmetros
    ----------
    img: ndarray
        Imagem onde texto será armazenado.
    bit: int, opcional
        Plano de bit onde o texto será armazenado. (padrão = 0)

    Retorno
    -------
    out: ndarray
        Imagem com texto codificado.
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

    # nova ordem, escrevendo em uma cor pr vez
    img = np.transpose(img, (2, 0, 1)).copy()
    # escrita do texto
    mascara = ~(np.ones(tam, dtype=np.uint8) << bit)
    img.flat[:tam] = (img.flat[:tam] & mascara) | (buffer << bit)

    # volta para a ordem H W D
    return np.transpose(img, (1, 2, 0))


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

def decodifica(img: Image, bit: int=0) -> str:
    """

    Parâmetros
    ----------
    img: ndarray
        Imagem onde texto foi armazenado.
    bit: int, opcional
        Plano de bit onde o texto foi armazenado. (padrão = 0)

    Retorno
    -------
    texto: str
        Texto recuperado.
    """
    # vetor de bits com o texto da imagem
    buffer = ((img.transpose((2, 0, 1)) >> bit) & 1).flat

    # recupera o tamanho do texto
    tamanho = int.from_bytes(junta_bits(buffer[:64]), 'big')
    # e o texto
    buf = junta_bits(buffer[64:][:tamanho * 8])

    # codificação em string
    return str(buf, encoding='utf8')
