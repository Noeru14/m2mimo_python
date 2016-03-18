/* main avec les differentes fonctions appelees en front */
function main(){
	
	menu = new menu();
	
}

function jouer(){
    $("body").css("text-align", "left");
    
    jouer = new jouer();
}

function regles(){
    $("body").css("text-align", "left");
    
    regles = new regles();
}

function score(){
    $("body").css("text-align", "left");
    
    score = new score();
}

function begin(){
    $("body").css("text-align", "left");
    gobanView = new GobanView();
   	goban = new JGoban();
    go = new Go();
    sidebar = new Sidebar();
	

    gobanView.animDrawGoban();

    $( "#console" ).html( "Debut de la partie, "+NAMEPLAYER[0]+" commence avec la couleur Noir\n" );
   // $( "#dialog" ).dialog( "open" );

//    $( "#dialog" ).html( "Debut de la partie, "+NAMEPLAYER[0]+" commence avec la couleur Noir" );
//    $( "#dialog" ).dialog( "open" );



}

