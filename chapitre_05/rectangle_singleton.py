
# HelloWorld => UpperCamelcase, PascalCase
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case


class Rectangle:
    
    _cpt = 0
    
    __slots__ = ['_longueur','_largeur']

    instance = None       # Attribut statique de classe
    
    
    def __new__(cls,*args,**kwargs): 
        "méthode de construction standard en Python"
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance
        
    def __init__(self,longueur=1,largeur=1):
        self._longueur = longueur 
        self._largeur = largeur 
        Rectangle._cpt += 1
    
    @classmethod
    def build_from_str(cls,value):
        lng, lrg = [int(i) for i in value.split(";")]
        
        # return cls(*[int(i) for i in value.split(";")])
        return cls(lng, lrg)
        
        
    @staticmethod
    def get_cpt():
        return Rectangle._cpt
        
    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur
    
    @property        
    def surface(self):
        return self._longueur*self._largeur
    
    
    def __str__(self):
        return f"{__class__.__name__} {self.longueur=}, {self.largeur=}"
    
    def __eq__(self,o):
        if not isinstance(o,type(self)):
            return False
        
        return self.longueur == o.longueur and self.largeur == o.largeur