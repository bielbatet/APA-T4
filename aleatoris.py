"""
Autor: Biel Batet Tudela
Descripció: Implementació de la generació de números aleatoris mitjançant
l'algoritme de Generació Lineal Congruent (LGC), tant amb una classe
iteradora (Aleat) com amb una funció generadora (aleat).
"""
 
 
class Aleat:
    """
    Generador de números aleatoris en el rang 0 <= x_n < m usant el mètode LGC.
 
    L'algoritme aplica iterativament la fórmula:
        x_{n+1} = (a * x_n + c) mod m
 
    Atributs:
        m (int): Mòdul (per defecte 2**48, estàndard POSIX).
        a (int): Multiplicador (per defecte 25214903917, estàndard POSIX).
        c (int): Increment (per defecte 11, estàndard POSIX).
        x0 (int): Llavor inicial (per defecte 1212121).
 
    Mètodes:
        __next__(): Retorna el següent número aleatori de la seqüència.
        __call__(llavor): Reinicia la seqüència amb la llavor indicada.
 
    Exemples:
        >>> rand = Aleat(m=32, a=9, c=13, x0=11)
        >>> for _ in range(4):
        ...     print(next(rand))
        16
        29
        18
        15
 
        >>> rand(29)
        >>> for _ in range(4):
        ...     print(next(rand))
        18
        15
        20
        1
    """
 
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        self.x0 = (self.a * self.x0 + self.c) % self.m
        return self.x0
 
    def __call__(self, llavor):
        self.x0 = llavor
 
 
def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Funció generadora de números aleatoris en el rang 0 <= x_n < m usant el mètode LGC.
 
    L'algoritme aplica iterativament la fórmula:
        x_{n+1} = (a * x_n + c) mod m
 
    Arguments:
        m (int): Mòdul (per defecte 2**48, estàndard POSIX).
        a (int): Multiplicador (per defecte 25214903917, estàndard POSIX).
        c (int): Increment (per defecte 11, estàndard POSIX).
        x0 (int): Llavor inicial (per defecte 1212121).
 
    Sortida:
        Genera una seqüència (potencialment infinita) de números enters
        en el rang [0, m). Si se li envia un valor amb send(), reinicia
        la seqüència usant aquest valor com a nova llavor.
 
    Exemples:
        >>> rand = aleat(m=64, a=5, c=46, x0=36)
        >>> for _ in range(4):
        ...     print(next(rand))
        34
        24
        38
        44
 
        >>> rand.send(24)
        38
        >>> for _ in range(4):
        ...     print(next(rand))
        44
        10
        32
        14
    """
    while True:
        x0 = (a * x0 + c) % m
        nova_llavor = yield x0
        if nova_llavor is not None:
            x0 = nova_llavor
 
 
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
