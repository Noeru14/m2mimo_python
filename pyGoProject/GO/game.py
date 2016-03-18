from GO import goban as GGoban

class Game:
    # Compteur de tour
    cpt_turn = 0

    # Creation objet goban
    # pour une partie
    Gpygoban = GGoban.Goban()

    # Sauvegarde une ancienne valeur
    # de x et y (sert pour le undo)
    histx = -1
    histy = -1

    # Si la valeur atteint deux
    # il est demande au joueur de confirmer
    # la fin de la partie
    passed = 0

    def __init__(self, id):
        self.id = id

    # COMMENCER UNE PARTIE > la partie s'enchaine a partir de cette fonction
    def start(self):
        self.turn()

    # TURN > si iteration 1 premier tour noir, si iteration 2 tour pair NOIR, si iteration 3 tour impair BLANC
    # gere si on souhaite JOUER, PASSER ou REPRENDRE SON COUP
    def turn(self):
        tour = self.cpt_turn+1 # sert a l'affichage du numero de tour
        if (self.cpt_turn == 0):
            print('~~~~ Tour : '+str(tour)+', Debut de la partie, a noir de commencer ! ~~~~')
        elif(self.cpt_turn%2 == 0):
            print('~~~~~~~~~~~~~~~~ Tour : '+str(tour)+' - Au tour de NOIR ~~~~~~~~~~~~~~~~')
        else:
            print('~~~~~~~~~~~~~~~~ Tour : '+str(tour)+' - Au tour de BLANC ~~~~~~~~~~~~~~~~')

        choice = -1

        while((int(choice) > 4) or (int(choice) < 1)):
            choice = input('Que souhaitez-vous faire ? JOUER (1) - '
                           'PASSER (2) - UNDO du joueur precedent (3) - ABANDONNER (4)\n')

            if(int(choice) == 1):
                x = input("Saisir ligne : ")
                y = input("Saisir colonne : ")
                self.histx = x
                self.histy = y
                OK = self.Gpygoban.move(x, y, self.cpt_turn)
                if(OK == 1):
                    self.cpt_turn += 1
                    self.passed = 0
                self.turn()

            elif(int(choice) == 2):
                self.passTurn()

            elif(int(choice) == 3):
                if((self.histx == -1) and (self.histy == -1)):
                    print('UNDO INTERDIT : impossible de undo le premier tour de jeu')
                else:
                    self.undo(self.histx, self.histy)

            elif(int(choice) == 4):
                self.resign()

            else:
                print('ERREUR SAISIE : saisir une valeur entre 1 et 4 inclus')

        """

        # TEST INPUT STONE SANS MENU (passer et undo)
        if(choice == 1):
            x = input("Saisir ligne : ")
            y = input("Saisir colonne : ")

            OK = self.Gpygoban.move(x, y, self.cpt_turn)
            if(OK == 1):
                self.cpt_turn += 1
            self.turn()
        """

    # PASSTURN > passer son tour
    def passTurn(self):
        if (self.cpt_turn %2 == 0):
            pl = 'noir'
        else:
            pl = 'blanc'

        print('INFO : Le tour de '+pl+' a ete passe')
        self.cpt_turn += 1
        self.passed += 1

        if(self.passed == 2):
            endgame = -1

            while((int(endgame) != 1) and (int(endgame) !=0)):
                endgame = input('INFO : Confirmez vous la fin de la partie (OUI = 1 / NON = 0) ? ')
                if((int(endgame) != 1) and (int(endgame) !=0)):
                    print('ERREUR SAISIE : vous devez saisir 1 ou 0')

            if(int(endgame) == 1):
                self.Gpygoban.end()
            else:
                self.passed -= 2
                self.turn()
        else:
            self.turn()

    # RESIGN > abandonner
    def resign(self):
        if (self.cpt_turn&2 == 0):
            print('ABANDON : Noir a abandonne la partie. Blanc gagne par abandon.')
        else:
            print('ABANDON : Blanc a abandonne la partie. Noir gagne par abandon.')

    # UNDO > reprendre son coup
    def undo(self, histx, histy):
        self.cpt_turn -= 1
        self.Gpygoban.undo(histx, histy)
        # self.turn()
