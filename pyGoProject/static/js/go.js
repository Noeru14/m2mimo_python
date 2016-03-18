/* fonction qui permet de calculer le score et qui est appele par la fonction sidebar */
function Go(){
 
    this.displayScore = function(){
        var tmp = go.getScore();
        
        if(!tmp){
            sidebar.showScore("Nobody", -1);
            return;
        }

        if(go.scoreBlack >= 185)
            sidebar.showScore(NAMEPLAYER[0], go.scoreBlack);
        else
            sidebar.showScore(NAMEPLAYER[1], go.scoreWhite);
    };
}
