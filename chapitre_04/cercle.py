import math
from icalcgeo import ICalcGeo
class Cercle(ICalcGeo):

    def __init__(self, rayon: int):
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon
    
    @rayon.setter
    def rayon(self,rayon):
        self._rayon=rayon

    @property
    def surface(self) -> float:
        return math.pi*self._rayon**2


    
