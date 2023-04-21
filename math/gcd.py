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

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    
    d, x, y = extended_euclid(b, a % b)
    
    return d, y, x - (a // b) * y

if __name__ == '__main__':
    a, b = 77, 444
    d, x, y = extended_euclid(b, a)
    revers = b + y
    
    print(f"{a}*{x} + {b}*{y} = {d}")
    print(revers)
    print(a * revers % b)
