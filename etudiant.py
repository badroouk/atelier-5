class etudiant :
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
 #list de type etudiant        
etudiant = [
{'nom' : 'alami','prenom' : 'alae', 'age': 25,'cne': 12222223, 'moyenne': 14},
{'nom' : 'alawi','prenom' : 'mohamed', 'age': 30,'cne': 489238923, 'moyenne': 16},
{'nom': 'zakaria','prenom' : 'tarik', 'age': 18,'cne': 12222233, 'moyenne': 9},
{'nom' : 'benaissa','prenom' : 'islam', 'age': 40,'cne': 1334342223, 'moyenne': 18},
]

#trie par age
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
#trie par moyenne
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)



