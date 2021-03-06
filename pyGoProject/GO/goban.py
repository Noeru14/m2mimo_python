class Goban:
    # goban
    pygoban = []

    # stocke le mouvement precedent
    # necessaire pour methode KO et cas suicide
    movex = -1
    movey = -1
    histox = -1
    histoy = -1

    # groupe de stockage : on peut capt jusqu a
    # 4 groupes en posant une piece
    group = [] # garde en memoire les coords d un groupe
    grouped = [] # permet de garder les zones traversees
    toAdd = [] # stock les ajouts a realiser

    capturedStones = [] # garde en memoire les coords d un groupe

    # determine combien de groupes on ete check
    cpt_group = 0

    # permet de ne pas compter un groupe plusieurs fois
    count_group = 0

    # permet de savoir si le move a conduit a une capt
    # 1 = oui, 0 = non
    capt = 0

    # permet de compter points
    points = 0
    bPoints = 0
    wPoints = 0

    # test fonctions
    functest = 0

    # test libertes
    okLiberties = 0

    # test KO - si nb pierres capturees = 1
    toCheck = 0
    isKO = 0
    a = -1
    b = -1
    captOneStone = 0
    checkedKO = 0

    def __init__(self):
        for i in range(19):
            self.pygoban.append([0]*19)

    def reset(self):
        self.pygoban = []
        self.movex = -1
        self.movey = -1
        self.histox = -1
        self.histoy = -1
        self.group = [] # garde en memoire les coords d un groupe
        self.grouped = [] # permet de garder les zones traversees
        self.toAdd = [] # stock les ajouts a realiser
        self.cpt_group = 0
        self.capt = 0
        self.points = 0
        self.bPoints = 0
        self.wPoints = 0
        self.functest = 0
        self.toCheck = 0
        self.isKO = 0
        self.a = -1
        self.b = -1
        self.captOneStone = 0
        self.checkedKO = 0
        for i in range(19):
            self.pygoban.append([0]*19)

    ### MOVE > execute a chaque mouvement
    ### gere toutes les regles de pose des pierres
    def move(self, x, y, z):
        self.histox = x
        self.histoy = y

        # definit si le mouvement est autorise ou non
        # verifie si la coordonnee est deja occupee
        occupied = self.isOccupied(x, y)

        if(occupied == 0):
            OK = 0
        else:
            OK = 1

        # Verifie si des pieces ont ete capturees
        if(OK == 1):
            # Necessaire pour verifier les libertes
            # le coup est a annuler si SUICIDAIRE OU nKO
            self.add(x, y, z)
            self.checkCapture(x ,y, z)

            if(self.capt == 0):

                # test necesaire pour la fx isSuicidal
                del self.group[:]
                del self.grouped[:]
                self.count_group = 0
                if(z%2 == 0):
                    z = 1
                else:
                    z = 2
                self.grouped.append((int(x), int(y)))
                OK = self.isSuicidal(x, y, z)

            elif(self.toCheck == 1):
                # Verifie si le deplacement ne respecte pas la regle du KO
                # <=> mouvement redondant
                OK = self.checkKO()

        if(OK == 0):
            if(z%2 == 0):
                val = 2
            else:
                val = 1

            # ANNULATION pour occupe
            if(occupied == 0):
                self.pygoban[int(self.histox)][int(self.histoy)] = val
            else:
                self.pygoban[int(x)][int(y)] = 0

            # ANNULATION pour KO
            if(self.capt == 1):
                self.pygoban[self.a][self.b] = val

        elif(self.checkedKO == 0):
            self.captOneStone = 0

        #self.displayGoban()

        # del self.group[:]
        # del self.grouped[:]
        # self.capt = 0
        self.toCheck = 0
        self.checkedKO = 0

        if(self.captOneStone < 2):
            self.movex = x
            self.movey = y

        return OK

    # ADD > ajoute le move au plateau
    def add(self, x, y, z):
        if(z%2 != 0):
            self.pygoban[int(x)][int(y)] = 2
        else:
            self.pygoban[int(x)][int(y)] = 1

    # DISPLAYGOBAN > affichage du plateau
    # sert pour tester
    def displayGoban(self):
        for i in range(19):
            print(self.pygoban[i])

    # ISOCCUPIED > verifie si la case est deja occupee
    def isOccupied(self, x, y):
        if(self.pygoban[int(x)][int(y)] != 0):
            print('MOVE INTERDIT : les coordonnees specifiees sont occupees !')
            return 0
        else:
            return 1

    # CHECKCAPTURE > verifie si il y a un risque
    # capture, si oui deroulement des methodes
    def checkCapture(self, x, y, z):
        # Permet de regarder autour de la piece jouee
        coords = [
            (int(x), int(y) - 1), #gauche
            (int(x) + 1, int(y)), #bas
            (int(x), int(y) + 1), #droite
            (int(x) - 1, int(y)), #haut
        ]

        # SI TOUR DE NOIR, on verifie si piece blanche autour
        # de la piece jouee, si oui, risque de capture
        if(z%2 == 0):
            val = 2
        else:
            val = 1

        for x, y in coords:
            if((-1 < int(x) < 19) and (-1 < int(y) < 19)):
                if (self.pygoban[x][y] == val):
                    # test si coord deja pris en compte
                    # dans un groupe
                    sameAdd = 0
                    for i in range(len(self.grouped)):
                        if(self.grouped[i] == (x, y)):
                            sameAdd = 1
                    if(sameAdd == 0):
                        self.grouped.append((x, y)) # stocke dans les groupes
                        self.defineGroup(x, y, val)
                        self.count_group = 0

    # DEFINEGROUP > definit un groupe a la fois
    def defineGroup(self, x, y, val):
        # Necessaire pour realiser des tests autour des pierres
        coords = [
            (int(x), int(y) - 1), #gauche
            (int(x) + 1, int(y)), #bas
            (int(x), int(y) + 1), #droite
            (int(x) - 1, int(y)), #haut
        ]

        # Sert a stocker les coordonnees d un groupe
        # les groupes sont traites un par un
        self.group.append((x, y))


        # Stocke les pierres dans un meme groupe
        for x, y in coords:
            if((-1 < int(x) < 19) and (-1 < int(y) < 19)):
                if(self.pygoban[x][y] == val):
                    same = 0
                    # Verifie si la coord a deja ete rajoute au groupe
                    for i in range(len(self.grouped)):
                        if(self.grouped[i] == (x, y)):
                            same = 1
                    if(same == 0):
                        self.toAdd.append((x, y))
                        self.grouped.append((x, y))

        # on ajoute a la liste de groupe les valeurs contenues
        # dans la liste toAdd progressivement
        if (len(self.toAdd) != 0):
            (a, b) = self.toAdd[0]
            del self.toAdd[0]
            self.defineGroup(a, b, val)

        # instructions executees si groupe completement defini
        if(self.count_group == 0):
            for testX in range(len(self.group)):
                # TEST contenu groupe
                print(self.group[testX])
            # TEST, A SUPPRIMER
            # test separateur de groupe, permet de voir combien de
            # fois la methode est lancee jusqu a cette etape
            # print('---')

            self.okLiberties = self.countLiberties()
            if ((self.okLiberties == 0) and (self.functest == 0)):
                pts = self.remove()
                self.calcCaptPoints(pts, val)
                self.capt = 1

            # test pour la methode isSuicidal
            if(self.functest == 0):
                del self.group[:]

        # Defini a un pour eviter de compter un groupe plusieurs fois
        # Il doit etre remis a zero pour definir un nouveau groupe
        self.count_group = 1

    # COUNTLIBERTIES > sert a compter les libertes d un groupe
    # si egal a 0, renvoi de 0
    def countLiberties(self):
        lib = 0

        for i in range(len(self.group)):
            (x, y) = self.group[i]

            coords = [
                (int(x), int(y) - 1), #gauche
                (int(x) + 1, int(y)), #bas
                (int(x), int(y) + 1), #droite
                (int(x) - 1, int(y)), #haut
            ]

            print('check : '+str(x)+', '+str(y)) #test

            for x, y in coords:
                if((-1 < int(x) < 19) and (-1 < int(y) < 19) and (lib == 0)):
                    if(self.pygoban[x][y] == 0):
                        lib += 1
                        print("added") #test
                        print(x, y) #test
                        print(self.pygoban[x][y])

        print('Lib test (1/0) : '+str(lib)) # test, a suppr
        return lib

    # ISSUICIDAL > verifie si un mouvement est suicidaire
    def isSuicidal(self, x, y, z):
        self.functest += 1
        print('into suic function')
        self.defineGroup(int(x), int(y), int(z))
        self.functest = 0
        self.count_group = 0

        if(int(self.okLiberties) == 1):
            print('not suic val : '+str(self.okLiberties)) # test
            return 1
        else:
            print('MOVE INTERDIT : vous ne pouvez pas '
                  'suicider une ou plusieurs pierres')
            return 0

    # REMOVE > supprime un groupe si les libertes sont nulles
    # et renvoie le nbre pierres supprimees
    def remove(self):
        x = 0

        for i in range(len(self.group)):
            (self.a, self.b) = self.group[i]
            self.capturedStones.append(self.group[i])
            self.pygoban[int(self.a)][int(self.b)] = 0
            x += 1
        if(x == 1):
            self.toCheck = 1
            self.captOneStone += 1
        else:
            self.captOneStone == 0
        return x # correspondant au nombre pierre(s) supprime pour calc pts

    # _REMOVE > utilise dans la definition des territoires
    # pour compter les territoires et les marquer
    # dans l interface il faudrait remplir par des croix au lieu de 9
    def _remove(self):
        x = 0

        for i in range(len(self.group)):
            (self.a, self.b) = self.group[i]
            self.pygoban[int(self.a)][int(self.b)] = 9
            x += 1

        return x # correspondant au nombre pierre(s) supprime pour calc pts

    # CHECKKO > verifie si un coup est KO
    def checkKO(self):
        print('checkKO launched '+str(self.captOneStone))
        self.checkedKO = 1

        if((int(self.a) == int(self.movex)) and (int(self.b) == int(self.movey))):
            print('is ko')
            self.isKO = 1
        else:
            self.isKO = 0

        if(self.isKO == 1 and self.captOneStone > 1):
            print('KO : vous ne pouvez pas capturer cette pierre pendant ce tour')
            return 0
        else:
            return 1

    def calcCaptPoints(self, pts, val):
        if(val == 2):
            self.bPoints += pts
            print('TOTAL points NOIR : '+str(self.bPoints)+' ; Noir gagne '+str(pts)+' point(s) !')
        else:
            self.wPoints += pts
            print('TOTAL points BLANC : '+str(self.wPoints)+' ; Blanc gagne '+str(pts)+' point(s) !')

    # UNDO > annule le coup de joueur precedent
    # et non celui du joueur actuel
    def undo(self, histx, histy):
        self.pygoban[int(histx)][int(histy)] = 0
        #self.displayGoban()

    # END > fin de la partie
    # enclenche le comptage des territories
    # annonce le joueur gagnant et arrete le programme
    def end(self):
    # PHASE 1 : definir les groupes morts
        # noir commence : dead w group
        # blanc : dead b group
        self.deadGroup()

    # PHASE 2 : definir les territoires (remplir par x)
        # noir ; saisir une case
        # blanc : saisir une case
        self.defTerritories()

    # PHASE 3 : affichage du score et annonce du gagnant
    #     self.displayScore()

    def deadGroup(self):
        print('PHASE 1 : definition des groupes morts')
        print('NOIR COMMENCE...')
        self.count_group = 1
        choix = -1
        turns = 0
        endOK = 1

        while((int(choix) != 3)):
            if(turns == 0):
                choix = input('PHASE 1 (noir) : ajouter un groupe mort (1), '
                              'ne plus ajouter - au tour de blanc (2)\n')
            else:
                choix = input('PHASE 1 (blanc) : ajouter un groupe mort (1), '
                              'fin de la procedure (3)\n')

            if(int(choix) == 1):
                x = input('Saisir la ligne d une pierre d un groupe mort : ')
                y = input('Saisir la colonne d une peirre d un groupe mort : ')

                # definit la valeur de groupe mort que l on peut supprimer
                if(turns == 0):
                    z = 2
                else:
                    z = 1

                # on verifie que noir ou blanc definit bien un groupe de couleur oppose
                if((turns == 0) and (self.pygoban[int(x)][int(y)] != 2)):
                    endOK = 0
                elif((turns == 1) and (self.pygoban[int(x)][int(y)] != 1)):
                    endOK = 0

                if(int(endOK) == 1):
                    self.grouped.append((int(x), int(y)))
                    self.defineGroup(x, y, z)
                    pts = self.remove()
                    self.calcCaptPoints(pts, z)
                    self.displayGoban()
                    del self.grouped[:]
                    del self.group[:]
                else:
                    print('ERREUR : la pierre selectionnee n est pas valide')

            elif(int(choix) == 2):
                if(turns == 0):
                    turns += 1
                else:
                    print('ERREUR : Fonction indisponible pour BLANC')

    def defTerritories(self):
        print('PHASE 2 : definition des territoires')
        print('NOIR COMMENCE...')
        choix = -1
        turns = 0
        z = 0
        endOK = 1

        while((int(choix) != 3)):
            if(turns == 0):
                choix = input('PHASE 1 (noir) : ajouter un territoire (1), '
                              'ne plus ajouter - au tour de blanc (2)\n')
            else:
                choix = input('PHASE 1 (blanc) : ajouter un territoire (1), '
                              'fin de la procedure (3)\n')

            if(int(choix) == 1):
                x = input('Saisir la ligne d une intersection : ')
                y = input('Saisir la colonne d une intersection : ')

                if(self.pygoban[int(x)][int(y)] == 9):
                    endOK = 0

                if(int(endOK) == 1):
                    self.grouped.append((int(x), int(y)))
                    self.defineGroup(x, y, z)
                    pts = self._remove()

                    if(turns == 0):
                        z = 2
                    else:
                        z = 1

                    self.calcCaptPoints(pts, z)
                    self.displayGoban()
                    del self.grouped[:]
                    del self.group[:]
                else:
                    print('ERREUR : vous ne pouvez pas redefinir un territoire')

            elif(int(choix) == 2):
                if(turns == 0):
                    turns += 1
                else:
                    print('ERREUR : Fonction indisponible pour BLANC')

    def displayScore(self):
        print('~~~~~~~~ SCORE ~~~~~~~~')
        print('Score de Noir : '+str(self.bPoints))
        print('Score de Blanc : '+str(self.wPoints))

        if(int(self.bPoints) > int(self.wPoints)):
            diff = int(self.bPoints) - int(self.wPoints)
            print('Noir gagne de '+str(diff)+' points !')
        elif(int(self.wPoints) > int(self.bPoints)):
            diff = int(self.wPoints) - int(self.bPoints)
            print('Blanc gagne de '+str(diff)+' points !')
        else:
            print('Egalite !')