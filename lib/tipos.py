"""
Procolos para tipagem estática com ``mypy``.
"""
from typing import (
    TYPE_CHECKING, overload,
    Type, Union, Tuple
)
from numpy import ndarray, uint8, bool as npbool

if TYPE_CHECKING:
    # Python 3.8+
    from typing import Literal
else:
    from collections import defaultdict
    # Python 3.7-
    Literal = defaultdict(lambda: 'tipo')
    Image = 'Image' # pylint: disable=invalid-name


class Bits(ndarray): # type: ignore
    """
    Vetor de bits representando texto.
    Os 64 bits iniciais são o tamanho do texto.
    """
    dtype: Type[uint8] = uint8
    ndim: Literal[1] = 1
    shape: Tuple[int]


class Indices(ndarray): # type: ignore
    """
    Vetor booleana de índices para acesso em outro `ndarray`.
    """
    dtype: Type[npbool] = npbool
    ndim: Literal[1] = 1
    shape: Tuple[int]


class Image(ndarray): # type: ignore # pylint: disable=function-redefined
    """
    Matrizes que representam imagens em OpenCV e bibliotecas similares.
    """
    dtype: Type[uint8] = uint8
    ndim: Literal[3] = 3
    shape: Tuple[int, int, Literal[3]]

    def copy(self) -> Image:
        ...

    @overload
    def __add__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __add__(self, other: Union[ndarray, float]) -> ndarray: ...
    def __add__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    @overload
    def __sub__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __sub__(self, other: Union[ndarray, float]) -> ndarray: ...
    def __sub__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    def __neg__(self) -> Image:
        ...

    def __pos__(self) -> Image:
        ...

    def __abs__(self) -> Image:
        ...

    def __invert__(self) -> Image:
        ...

    @overload
    def __mul__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __mul__(self, other: Union[ndarray, float]) -> ndarray: ...
    def __mul__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    def __matmul__(self, other: ndarray) -> ndarray:
        ...

    @overload
    def __pow__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __pow__(self, other: Union[ndarray, float]) -> ndarray: ...
    def __pow__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    @overload
    def __floordiv__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __floordiv__(self, other: ndarray) -> ndarray: ...
    def __floordiv__(self, other: Union[ndarray, int]) -> ndarray:
        ...

    def __truediv__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    @overload
    def __mod__(self, other: Union[Image, int]) -> Image: ...
    @overload
    def __mod__(self, other: Union[ndarray, float]) -> ndarray: ...
    def __mod__(self, other: Union[ndarray, float]) -> ndarray:
        ...

    def __rshift__(self, other: Union[Image, int]) -> Image:
        ...

    def __lshift__(self, other: Union[Image, int]) -> Image:
        ...

    def __and__(self, other: Union[Image, int]) -> Image:
        ...

    def __xor__(self, other: Union[Image, int]) -> Image:
        ...

    def __or__(self, other: Union[Image, int]) -> Image:
        ...
