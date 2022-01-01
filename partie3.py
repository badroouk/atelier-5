class Utilisateur:

    _nom = ""
    _email = ""
    _mot_de_passe = ""
    _genre = ""
    _age = 0

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
        self._nom = nom
        self._email = email
        self._mot_de_passe = mot_de_passe
        self._genre = genre
        self._age = age

    def display(self):
        print(self._nom, "\t", self._email, "\t", self._mot_de_passe, "\t", self._genre, "\t", self._age)


class Module:

    __nom = 0
    __volume_horaire = 0
    __semestre = ""
    ListMatiere = []
    def __init__(self, nom="", volume_horaire=0, semestre=""):
        self.__nom = nom
        self.__volume_horaire = volume_horaire
        self.__semestre = semestre

    def display(self):
        print(self.__nom, "\t", self.__volume_horaire, "\t", self.__semestre)


class Professeur(Utilisateur):

    __ppr = 0
    __grade = ""
    module = Module()
    ListeMatieres = []
    ListeAnnesAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
        super().__init__(self, nom, email, mot_de_passe, genre, age)
        self.__ppr = ppr
        self.__grade = grade

    def display(self):
        print(self.__ppr, "\t", self.__grade)


class Matiere:

    __nom = 0
    __pourcentage = 0
    module = Module()
    ListeAnnesAcademique = []
    def __init__(self, nom="", pourcentage=0):
        self.__nom = nom
        self.__pourcentage = pourcentage

    def display(self):
        print(self.__nom, "\t", self.__pourcentage)


class Annee_Academique:

    __anne = ""
    Listetudiant = []
    Listematiesre = []
    Listeprofesseur = []

    def __init__(self, anne=""):
        self.__anne = anne

    def display(self):
        print(self.__anne)


class Etudiant(Utilisateur):

    __code_massar = ""
    ListAnneAcademique = []

    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
        super().__init__(nom, email, mot_de_passe, genre, age)
        self.__code_massar = code_massar

    def display(self):
        print(self.__code_massar)


class Evaluation:

    _note = 0
    matiere = Matiere()
    annee_acadimique = Annee_Academique()
    etudiant = Etudiant()

    def __init__(self, note=0):
        self._note = note

    def display(self):
        print(self._note)


