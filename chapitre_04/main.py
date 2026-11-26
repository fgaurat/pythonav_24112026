from pprint import pprint
from carre import Carre
from cercle import Cercle
from rectangle import Rectangle
from isurface import ISurface


def show_surface(o:ISurface):
    print(o.surface)

def main():
    c = Carre()
    c1 = Carre(2)
    # region
    print(c1.cote)
    print(c1.surface)
    c1.cote = 12
    print(c1.surface)
    # endregion
    r = Rectangle(2,3)
    ce = Cercle(2)
    print(ce.surface)
    show_surface(r)
    show_surface(c)
    show_surface(c1)
    show_surface(ce)

if __name__=='__main__':
    main()
