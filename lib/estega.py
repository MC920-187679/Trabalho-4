from typing import Iterator
from tipos import Image, Bits
import numpy as np


def para_bytes(texto: str) -> Bits:
    texto_buf =  texto.encode('utf8')
    tamanho = len(texto_buf).to_bytes(8, 'big')

    buffer = np.asarray(tuple(tamanho + texto_buf), dtype=np.uint8)
    buf = np.zeros((8, len(buffer)), dtype=np.uint8)
    for i in range(8):
        buf[i] = buffer & 1
        buffer = buffer >> 1

    return buf.T.ravel()

def codifica(img: Image, texto: str, bit: int=0) -> Image:
    buffer = para_bytes(texto)
    tam = len(buffer)
    if tam > img.size:
        imgh, imgw, _ = img.shape
        limite = img.size // 8

        descr = f'imagem {imgh}x{imgw} consegue armazenar no máximo {limite} bytes'
        raise OverflowError(f'{descr}, texto tem {tam // 8} bytes')

    mascara = ~(np.ones(tam, dtype=np.uint8) << bit)
    img.flat[:tam] = (img.flat[:tam] & mascara) | (buffer << bit)
    return img


def junta(bits: Bits) -> bytes:
    bit = np.reshape(bits, (-1, 8)).T
    buf = np.zeros_like(bit[0])

    for i in range(8):
        buf |= bit[i] << i
    return bytes(buf)

def de_bytes(buffer: Bits) -> str:
    tamanho = int.from_bytes(junta(buffer[:64]), 'big')
    buffer = junta(buffer[64:][:tamanho * 8])

    return str(buffer, encoding='utf8')

def decodifica(img: Image, bit: int=0) -> str:
    buffer = (img >> bit) & 1
    return de_bytes(buffer.flat)
