"""
Funções de codificação e decodificação para esteganografia.
"""
from typing import Optional
import numpy as np
from .tipos import Image, Bits


# # # # # # # #
# CODIFICAÇÃO #

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


def codifica_em_bit(img: Image, buffer: Bits, bit: int) -> Optional[Bits]:
    """
    Codifica parte do buffer em um plano de bit, retornando o buffer restante.
    """
    # buffer cabe no plano
    if len(buffer) <= img.size:
        tam = len(buffer)
        # sem resto
        resto = None
    # senão, armazena parte do buffer
    else:
        tam = img.size
        buffer, resto = buffer[:tam], buffer[tam:]

    # armazenamento na imagem
    mascara = ~(np.ones(tam, dtype=np.uint8) << bit)
    img.flat[:tam] = (img.flat[:tam] & mascara) | (buffer << bit) # pylint: disable=E1137

    return resto


def codifica(img: Image, texto: bytes, bit: Optional[int]=None) -> Image:
    """
    Codifica arquivo dentro da imagem, no plano de bits especificado.

    Parâmetros
    ----------
    img: ndarray
        Imagem onde arquivo será armazenado.
    texto: bytes
        Vetor de bytes do arquivo.
    bit: int, opcional
        Plano do bit de armazenamento.
        Padrão é todos, começando do menos significativo.

    Retorno
    -------
    out: ndarray
        Imagem com arquivo codificado.
    """
    # vetor de bits do texto
    buffer = separa_bits(texto)

    # escrita do arquivo
    if bit is not None:
        buffer = codifica_em_bit(img, buffer, bit)
    else:
        # escreve em todos os bits, começando do menos significativo
        for i in range(8):
            buffer = codifica_em_bit(img, buffer, i)
            # encerra quando o buffer acaba
            if buffer is None:
                break

    # buffer maior que capacidade, sobrou uma parte
    if buffer is not None:
        raise OverflowError('arquivo muito grande para a imagem')

    return img


# # # # # # # # #
# DECODIFICAÇÃO #

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

def plano_bit(img: Image, bit: int) -> Bits:
    """
    Acessa um plano de bit da imagem.
    """
    return ((img >> bit) & 1).ravel('C')


def decodifica(img: Image, bit: int=0) -> bytes:
    """
    Decodifica arquivo armazenado na imagem.

    Parâmetros
    ----------
    img: ndarray
        Imagem onde arquivo foi armazenado.
    bit: int, opcional
        Plano do bit de armazenamento.
        Padrão é todos, começando do menos significativo.

    Retorno
    -------
    texto: bytes
        Arquivo recuperado.
    """
    if bit is not None:
        # buffer é apenas um plano
        buffer = plano_bit(img, bit)
    else:
        # buffer são todos os planos
        bits = [plano_bit(img, b) for b in range(8)]
        buffer = np.concatenate(bits)

    # recupera o tamanho do texto
    tamanho = int.from_bytes(junta_bits(buffer[:64]), 'big')
    # e o texto
    return junta_bits(buffer[64:][:tamanho * 8])
