var SIZE = 25;
var LINENUM = 19;
var GOBANHEIGHT = SIZE*(LINENUM-1);
var GOBANWIDTH = SIZE*(LINENUM-1);
var CANVASHEIGHT = GOBANHEIGHT + 2*SIZE;
var CANVASWIDTH = GOBANWIDTH + 2*SIZE;
var BACKGROUNDCOLOR = 'rgb(242, 193, 48)';
var BACKGROUNDFONT = '12px Sans-serif';
var COLORBLACK = '#000000';
var COLORWHITE = '#FFFFFF';
var STONECOLOR = [COLORBLACK, COLORWHITE];
var STONEIMG = ["static/img/stoneBlack.png", "static/img/stoneWhite.png"];


var DIRECTION = new Array([-1, 1, 0, 0], [0, 0, -1, 1]); 

var THIS;

var PARTYNAME="nom";

var NAMEPLAYER = ["Joueur 1", "Joueur 2"];

var PASSCPT= 0;

//var PLAYERNUM= 0;
//var PHASE= 0;

var CANVAS;

