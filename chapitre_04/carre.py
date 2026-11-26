from rectangle import Rectangle

class Carre(Rectangle):
    
    
    def __init__(self,cote=1):
        super().__init__(cote,cote)
        self._cote = cote  
    
    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,cote):
        self._cote = cote
        self.longueur = cote
        self.largeur = cote
    