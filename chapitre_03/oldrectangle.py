
# HelloWorld => UpperCamelcase, PascalCase
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case


class Rectangle:
    
    
    def __init__(self,longueur=1,largeur=1):
        self._longueur = longueur 
        self._largeur = largeur 
        
    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur
    
    def set_longueur(self,longueur):
        self._longueur = longueur

    def set_largeur(self,largeur):
        self._largeur = largeur
        
    def get_surface(self):
        return self._longueur*self._largeur
    
    longueur = property(get_longueur,set_longueur,doc="Propriété longueur")
    largeur = property(get_largeur,set_largeur,doc="Propriété largeur")
    surface = property(get_surface,doc="Propriété surface")