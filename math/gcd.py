from __future__ import annotations
import abc
import typing

class ModAble(abc.ABC):
    @abc.abstractmethod
    def __mod__(self, other): ...

MA = typing.TypeVar('MA', bound=ModAble)

class ModAbleComplex(ModAble, complex):
    def __mod__(self, other: ModAbleComplex) -> ModAbleComplex:
        quotient = self / other
        quotient = self.from_complex(quotient)

        return self.from_complex(self - (quotient * other))
    
    @classmethod
    def from_complex(cls, _complex: complex) -> ModAbleComplex:
        return cls(round(_complex.real), round(_complex.imag))

def gcd(a: MA, b: MA) -> MA:
    r = a % b
    
    while r != 0:
        a = b
        b = r
        r = a % b

    return b

if __name__ == '__main__':
    a = ModAbleComplex(32, 9)
    b = ModAbleComplex(4, 11)
    result = gcd(a, b)

    print(result)