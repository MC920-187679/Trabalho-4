"""
Funções de IO com as imagens.
"""
import numpy as np
import cv2
from .tipos import Image


def imgread(arquivo: str) -> Image:
    """
    Lê um arquivo de imagem em escala de cinza.

    Parâmetros
    ----------
    arquivo: str
        Caminho para o arquivo de imagem a ser lido.

    Retorno
    -------
    img: ndarray
        Matriz representando a imagem lida.

    Erro
    ----
    OSError
        Arquivo não pode ser lido ou não existe.
    ValueError
        Arquivo não pode ser decodificado como imagem.
    """
    # abre o arquivo fora do OpenCV, para que o
    # Python trate os erros de IO
    with open(arquivo, mode='rb') as filebuf:
        buf = np.frombuffer(filebuf.read(), dtype=np.uint8)

    # só resta tratar problemas de decodificação
    img: Image = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    if img is None:
        msg = f'não foi possível parsear "{arquivo}" como imagem'
        raise ValueError(msg)

    return img


def imgwrite(img: Image, arquivo: str) -> None:
    """
    Escreve uma matriz como imagem PNG ou PGM em um arquivo.

    Parâmetros
    ----------
    img: ndarray
        Matriz representando uma imagem.
    arquivo: str
        Caminho para o arquivo onde a imagem será gravada.

    Erro
    ----
    ValueError
        A images não pode ser salva no arquivo ou a entrada não
        representa uma imagem.
    """
    if not cv2.imwrite(arquivo, img):
        msg = f'não foi possível salvar a imagem em "{arquivo}"'
        raise ValueError(msg)


def imgshow(img: Image, nome: str="", delay: int=250) -> None:
    """
    Apresenta a imagem em uma janela com um nome.

    Parâmetros
    ----------
    img: ndarray
        Matriz representando uma imagem.
    nome: str, opcional
        Nome da janela a ser aberta.
    delay: int, opcional
        Tempo em milisegundos de checagem da janela.
    """
    try:
        cv2.namedWindow(nome, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(nome, img)

        # espera alguma chave ou a janela ser fechada
        while cv2.waitKey(delay) < 0:
            # problemas com versões diferentes de python e opencv
            prop1 = cv2.getWindowProperty(nome, cv2.WND_PROP_ASPECT_RATIO)
            prop2 = cv2.getWindowProperty(nome, cv2.WND_PROP_VISIBLE)
            if prop1 == prop2:
                break
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    # Ctrl-C não são erros nesse caso
    except KeyboardInterrupt:
        pass
