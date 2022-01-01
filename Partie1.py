# Classe Vecteur2D avec un constructure
class Vecteur2D:
    # Vecteur plans
    def __init__(self, x0=0, y0=0):
        # Constructeur avec parametres par defaut.
        self.x = x0  # initialisation de x et y, attributs d'instance
        self.y = y0

    def __str__(self):
        # Utilisation du print
        return "x = %d, y = %d" % (self.x, self.y)


# programme principale
if __name__ == '__main__':
    print(" une instance par defaut ")
    print(Vecteur2D())
    print(" une instance initialisee ")
    print(Vecteur2D(8.9, 4.1))

# Surcharge des opérateurs


class Vecteur2D(object):
    # Définition d'une classe."""
    def __init__(self, x0=0, y0=0):
        # Constructeur avec paramètres par défaut.
        self.x = x0  # initialisation de x et y, attributs d'instance
        self.y = y0

    # Addition vectorielle.
    def __add__(self, other):
        return Vecteur2D(self.x+other.x, self.y+other.y)

    # Affichage d'un Vecteur2D.
    def __str__(self):
        return "Vecteur(%d, %d)" % (self.x, self.y)


# programme principal -----------------------------------------------
vect1, vect2 = Vecteur2D(1.2, 2.3), Vecteur2D(3.4, 4.5)
print(vect1)
print(vect2)
print(vect1 + vect2)

# classe des rectangles.


class Rectangle():
    # Constructeur avec valeurs par défaut
    def __init__(self, longueur=30, largeur=15):
        self.Longueur = longueur
        self.Largeur = largeur
        self.nom = "rectangle"
    # Calcule la surface d'un rectangle.

    def surface(self):
        return self.Longueur*self.Largeur
    # Affichage des caractéristiques d'un rectangle.

    def __str__(self):
        return "\nLe %s de longueur %s et largeur %s a une surface de %s" % (self.nom, self.Longueur, self.Largeur, self.surface())

# classe des carrés (hérite de Rectangle).


class Carre(Rectangle):
    # Constructeur avec valeur par défaut
    def __init__(self, cote=10):
        Rectangle.__init__(self, cote, cote)
        self.nom = "carré"  # surchage d'attribut d'instance


# programme principale
if __name__ == '__main__':
    r = Rectangle(12, 8)
    print(r)
    c = Carre()
    print(c)

# classe des points du plan.


class Point():
    # Constructeur avec valeurs par défaut
    def __init__(self, x=0.0, y=0.0):
        self.px = float(x)
        self.py = float(y)
# classe Héritage la classe point.


class Segment():
    # Le constructeur utilise deux objets Point.
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)

    def __str__(self):
        return "Segment : [(%d, %d), (%d, %d)]" % (self.orig.px, self.orig.py, self.extrem.px, self.extrem.py)


# programme principale
if __name__ == '__main__':
    s = Segment(1, 2, 3, 4)
    print(s)
