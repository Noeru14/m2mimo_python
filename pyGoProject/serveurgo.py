import sys
import cherrypy
import os
import json
import routes
import cgi, cgitb


from jinja2 import Environment, FileSystemLoader, PackageLoader
from GO import goban as example
from GO import game as example1

goban1 = example.Goban()

game = None
#env = Environment()

env = Environment(loader=PackageLoader('serveurgo', 'templates'))

cgitb.enable()
form = cgi.FieldStorage()

game = example1.Game(0)

class Root:
    # index du site
    @cherrypy.expose
    def index(self):
        game.Gpygoban.reset()
        game.cpt_turn = 0
        game.histx = -1
        game.histy = -1
        game.passed = 0

        tmpl = env.get_template("index.html")
        game.Gpygoban.displayGoban()
        return tmpl.render()

class actions:
    # envoie le score au serveur
    @cherrypy.expose
    def score(self):
        if(int(game.Gpygoban.bPoints) > int(game.Gpygoban.wPoints)):
            diff = int(game.Gpygoban.bPoints) - int(game.Gpygoban.wPoints)
            print('Noir gagne de '+str(diff)+' points !')
            response={'console' : 'Noir gagne de '+str(diff)+' points !'}
            return json.dumps(response)
        elif(int(game.Gpygoban.wPoints) > int(game.Gpygoban.bPoints)):
            diff = int(game.Gpygoban.wPoints) - int(game.Gpygoban.bPoints)
            print('Blanc gagne de '+str(diff)+' points !')
            response={'console' : 'Blanc gagne de '+str(diff)+' points !'}
            return json.dumps(response)
        else:
            print('Egalite !')
            response={'console' : 'Egalite !'}
            return json.dumps(response)

    # passe action au prochain joueur
    @cherrypy.expose
    def passTurn(self):
        if (game.cpt_turn %2 == 0):
            pl = 'noir'
        else:
            pl = 'blanc'

        print('INFO : Le tour de '+pl+' a ete passe')
        game.cpt_turn += 1
        game.passed += 1
        game.Gpygoban.displayGoban()
        response={'console' : 'INFO : Le tour de '+pl+' a ete passe'}
        return json.dumps(response)

    # place une pierre sur le plateau
    @cherrypy.expose
    def move(self, posX, posY):
        x = posX
        y = posY

        OK = game.Gpygoban.move(x, y, game.cpt_turn)
        tempColor=0
        if(game.cpt_turn%2 == 1):
            color = "white";
            tempColor=1
        else:
            color = "black";
            tempColor=0

        response={'console' :  color + ' stone placed'}
        response["bool"]= 0

        if(OK == 1):
            game.cpt_turn += 1
            game.passed = 0
            response["bool"]= 1
            game.histx = x
            game.histy = y

        response["stones"]={}
        response["color"]=tempColor

        if(game.Gpygoban.capt and OK):

            tempcpt = 0
            while tempcpt < len(game.Gpygoban.capturedStones):

                response["stones"][tempcpt]={'x':game.Gpygoban.capturedStones[tempcpt][1],'y':game.Gpygoban.capturedStones[tempcpt][0]}
                tempcpt += 1

        game.Gpygoban.displayGoban()
        print(game.Gpygoban.capturedStones)

        game.Gpygoban.capt = 0
        del game.Gpygoban.capturedStones[:]
        del game.Gpygoban.group[:]
        del game.Gpygoban.grouped[:]
        return json.dumps(response)

    # reprend le dernier coup
    @cherrypy.expose
    def undo(self):
        if((game.histx == -1) and (game.histy == -1)):
            print('UNDO INTERDIT : impossible de undo le premier tour de jeu')
            response={'console' : 'UNDO INTERDIT : impossible de undo le premier tour de jeu'}

        elif(game.Gpygoban.pygoban[int(game.histx)][int(game.histy)] == 0):
            response={'console' : 'vous pouvez pas annuler plus d\'une action', 'x' : game.histx, 'y' : game.histy }
        else:
            game.undo(game.histx, game.histy)
            response={'console' : 'last stone removed', 'x' : game.histx, 'y' : game.histy }

        game.Gpygoban.displayGoban()
        return json.dumps(response)

    #end game
    @cherrypy.expose
    def endGame(self):
        response={'console' : 'PHASE 1 : definition des groupes morts\n'}
        response['console']+='NOIR COMMENCE...'
        response['phase'] = 1
        response['player'] = 1
        return json.dumps(response)

    # selection des groupes morts
    @cherrypy.expose
    def selectDeadGroup(self,x,y,z):
        response={'console':""}
        response["bool"]=0
        game.Gpygoban.count_group = 1
        # choix = -1
        turns = 0
        endOK = 1

        # on verifie que noir ou blanc definit bien un groupe de couleur oppose
        if((turns == 0) and (game.Gpygoban.pygoban[int(x)][int(y)] != z)):
            endOK = 0

        if(int(endOK) == 1):
            response["bool"]=1
            game.Gpygoban.grouped.append((int(x), int(y)))
            game.Gpygoban.capturedStones.append((int(x), int(y)))
            game.Gpygoban.defineGroup(x, y, z)
            pts = game.Gpygoban.remove()
            game.Gpygoban.calcCaptPoints(pts, z)
            game.Gpygoban.displayGoban()
            tempcpt = 0
            while tempcpt < len(game.Gpygoban.capturedStones):

                response["stones"][tempcpt]={'x':game.Gpygoban.capturedStones[tempcpt][1],'y':game.Gpygoban.capturedStones[tempcpt][0]}
                tempcpt += 1
            del game.Gpygoban.capturedStones[:]
            del game.Gpygoban.grouped[:]
            del game.Gpygoban.group[:]

        else:
            print('ERREUR : la pierre selectionnee n est pas valide')
            response['console'] = 'ERREUR : la pierre selectionnee n est pas valide'
            response["bool"]=0
        return json.dumps(response)





dispatcher = None

# route management urls in the website
def setup_routes():
    d = cherrypy.dispatch.RoutesDispatcher()
    d.connect('index', '/', controller=Root, action='index')
    d.connect('move', '/move', controller=actions(), action='move')
    d.connect('passTurn', '/passTurn', controller=actions(), action='passTurn')
    d.connect('quit', '/quit', controller=actions(), action='quit')
    d.connect('undo', '/undo', controller=actions(), action='undo')
    d.connect('score', '/score', controller=actions(), action='score')
    d.connect('endGame', '/endGame', controller=actions(), action='endGame')
    dispatcher = d
    return dispatcher

current_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
# configuration of the plugin cherrypy
config = {
    'global': {

        'log.screen': True,
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 2000,
        'engine.autoreload_on': False,
        'log.error_file': os.path.join(current_dir, 'errors.log'),
        'log.access_file': os.path.join(current_dir, 'access.log'),
    },
    '/':{
        'tools.staticdir.root' : current_dir,
        'request.dispatch': setup_routes()
    },
    '/static':{
        'tools.staticdir.on' : True,
        'tools.staticdir.dir' : 'static',
    },
}
server_config = {
    'server.socket_port': 2000,
    'engine.autoreload_on': False
}

cherrypy.quickstart(Root(), '/', config)

