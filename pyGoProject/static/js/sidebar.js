/* fonction qui affiche la barre sur le cote du plateau */

function Sidebar(){
    this.setPlayer = function(str){
        $("#playerCurLi").text("Joueur actuel: \n" + str);
    };

    this.setPartyName = function(str){
        $("#partyName").text("Partie : \n" + PARTYNAME);
    };

    this.setNumCur = function(str){
        $("#numCurLi").text("Coups: \n" + str);
    };

    this.showScore = function(player, score){
        if(score === -1){
            $("#playerCurLi").text("The Game is not over.");
            return;
        }

        $("#playerCurLi").text("Victor: \n" + player);
        $("#numCurLi").text("Victor Score: \n" + score);
    };

    this.div = document.createElement("div");
    this.div.className = "divSidebar";

    this.list = document.createElement("ul");
    this.list.className = "listSidebar";

 	// faire lien avec nom partie de jouer
    var partyName = document.createElement("li");
    partyName.id= "partyName";
    partyName.innerHTML = "Partie : \n"+PARTYNAME;
    $(this.list).append(partyName);

    // nom du joueur qui doit jouer
    var playerCur = document.createElement("li");
    playerCur.id= "playerCurLi";
    playerCur.innerHTML = "Joueur actuel : \n" + NAMEPLAYER[0];
    $(this.list).append(playerCur);

    var numCur= document.createElement("li");
    numCur.id= "numCurLi";
    numCur.innerHTML = "Coups : \n 0";
    $(this.list).append(numCur);

    // bouton passer
    this.passerBtn = document.createElement("a");
    this.passerBtn.className = "scoreBtn button button-rounded button-flat-primary";
    this.passerBtn.innerHTML = "Passer";
    this.passerBtn.href = "#";
    this.passerBtn.id = "passID";


    // bouton quit
    this.quitBtn = document.createElement("a");
    this.quitBtn.className = "scoreBtn button button-rounded button-flat-primary";
    this.quitBtn.innerHTML = "Quit";
    this.quitBtn.href = "#";
    this.quitBtn.id = "quitID";

	//this.passerBtn.addEventListener('click', this.Pass);

    //bouton undo
    this.undoBtn = document.createElement("a");
    this.undoBtn.className = "scoreBtn button button-rounded button-flat-primary";
    this.undoBtn.innerHTML = "Undo";
    this.undoBtn.href = "#";
    this.undoBtn.id = "undoID";
	//this.passerBtn.addEventListener('click', this.Undo);

	// bouton score
    this.scoringBtn = document.createElement("a");
    this.scoringBtn.className = "scoreBtn button button-rounded button-flat-primary";
    this.scoringBtn.innerHTML = "Score";
    this.scoringBtn.href = "#";
    this.scoringBtn.id = "scoreID";
	//this.passerBtn.addEventListener('click', this.Score);

    // bouton menu
    this.menuBtn = document.createElement("a");
    this.menuBtn.className = "scoreBtn button button-rounded button-flat-primary";
    this.menuBtn.innerHTML = "Menu";
    this.menuBtn.id = "menu";
    this.menuBtn.href = "#";
	//this.passerBtn.addEventListener('click', this.Menu);

    $(this.div).append(this.list);
    $(this.div).append(this.undoBtn);
    $(this.div).append(this.passerBtn);
    $(this.div).append(this.scoringBtn);
    $(this.div).append(this.menuBtn);
    $(this.div).append(this.quitBtn);
   	$("body").append(this.div);

//     $( "#popupinformation" ).dialog({
//        autoOpen: false,
//        width: 400,
//        buttons: [
//            {
//                text: "OK",
//                click: function() {
//                    $( this ).dialog( "close" );
//                }
//            }
//        ]
//    });
	dialog = document.createElement("div");
    dialog.id = "dialog";
    $("body").append(dialog);
//     $( "#dialog" ).dialog({
//        autoOpen: false,
//        width: 400,
//        buttons: [
//            {
//                text: "OK",
//                click: function() {
//                    $( this ).dialog( "close" );
//                }
//            }
//        ]
//    });

    // autres boutons en html
    $(".divSidebar").append("<div id=\"consoleDIV\" align=\"left\"><textarea style=\"resize: none;\" id=\"console\" readonly rows='6'  ></textarea></div>");
    $('.divSidebar').click(false);
    $("body").append('<div id="myModal" class="modal fade"> <div class="modal-dialog"> <div class="modal-content"> <div class="modal-header"> <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button> <h4 class="modal-title">Message</h4> </div> <div class="modal-body"> <p>Do you want to save changes you made to document before closing?</p> <p class="text-warning"><small>If you don\'t save, your changes will be lost.</small></p> </div> <div class="modal-footer"> <button type="button" class="btn btn-default" data-dismiss="modal">Close</button> <button type="button" class="btn btn-primary">Save changes</button> </div> </div> </div> </div>');



    $( "#menu" ).click(function( event ) {

        event.preventDefault();
    });
   $( "#undoID" ).click(function( event ) {
          $.ajax( {
			type: "POST",
			url: "/undo",
			data: { },
			success: function(data)
             {  var data = jQuery.parseJSON( data );

                $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");

                $('#console').scrollTop($('#console')[0].scrollHeight);


                goban.stonesOnGoban[data.y][data.x] = null;

                goban.stones10[data.y][data.x] = -1;
                goban.turn--;
                goban.numCurrent--;
                gobanView.reDraw();
                sidebar.setPlayer(NAMEPLAYER[goban.turn % 2]);
                sidebar.setNumCur(goban.turn);


             }
		});
        event.preventDefault();
    });

     $( "#scoreID" ).click(function( event ) {
          $.ajax( {
			type: "POST",
			url: "/score",
			data: {},
			success: function(data)
             {  var data = jQuery.parseJSON( data );

                $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");

                $('#console').scrollTop($('#console')[0].scrollHeight);

             }
		});
        event.preventDefault();
    });

    $( "#passID" ).click(function( event ) {
        goban.turn += 1;
        PASSCPT += 1;

        if(PASSCPT==2){

            $(".modal-body").html('<p class="text-warning">Terminer la partie ?</p>');
            $(".modal-footer").html('<button type="button" class="btn btn-success" onclick="$(\'#myModal\').modal(\'hide\')"  >NO</button> <button onclick="endGame();$(\'#myModal\').modal(\'hide\');" type="button" class="btn btn-error">YES</button>');

            $("#myModal").modal('show');



            PASSCPT=0;
        }

          $.ajax( {
			type: "POST",
			url: "/passTurn",
			data: {},
			success: function(data)
             {
                var data = jQuery.parseJSON( data );
                 if(data.hasOwnProperty('console') && typeof data.console != 'undefined' ){
                    $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");

                    $('#console').scrollTop($('#console')[0].scrollHeight);
                 }
//                console.debug(data);
             }
		});
        event.preventDefault();
    });

//	this.clickFinishBtn = function(evt) {
//		PHASE +=1;
//		PLAYERNUM +=1;
//		if(PHASE==2){
//			alert("shit phase 2")
//		}
//		}
//	}

    $( "#quitID" ).click(function( event ) {
          $.ajax( {
			type: "POST",
			url: "/quit",
			data: { },
			success: function(data)
             {  var data = jQuery.parseJSON( data );
                //alert( obj.name === "John" );
                $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");

                $('#console').scrollTop($('#console')[0].scrollHeight);
//                PLAYERNUM = data.player;
//                PHASE = data.phase;
//                $( "#consoleDIV" ).append('<button id="finishBtn" type="button" class="btn btn-warning">FINISH</button>');
//
//                CANVAS.addEventListener('click', this.selectDeadGroupClick);

             }
		});
        event.preventDefault();
    });
//    this.selectDeadGroupClick = function(evt) {
//        var point = toPoint(evt.layerX, evt.layerY);
//        var x = point[0];
//        var y = point[1];
//        if (x < 0 || x >= LINENUM)
//            return;
//        if (y < 0 || y >= LINENUM)
//            return;
//
//        $.ajax( {
//			type: "POST",
//			url: "/selectDeadGroup",
//			data: { x:y ,y:x,z:PLAYERNUM },
//			success: function(data)
//             {  var data = jQuery.parseJSON( data );
//
//                if(data.bool==0){
//
//                    $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");
//
//                    $('#console').scrollTop($('#console')[0].scrollHeight);
//                    return
//                }
//				$.each(data.stones, function( index, value ) {
//                    goban.stonesOnGoban[value.x][value.y] = null;
//                    goban.stones10[value.x][value.y] = -1;
//                });
//
//                $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");
//
//                $('#console').scrollTop($('#console')[0].scrollHeight);
//
//				gobanView.reDraw();
//             }
//		});

}
function endGame(){
    $.ajax( {
			type: "POST",
			url: "/endGame",
			data: { },
			success: function(data)
             {  var data = jQuery.parseJSON( data );

                $( "#console" ).html($( "#console" ).text()+"\n"+data.console +"\n");

                $('#console').scrollTop($('#console')[0].scrollHeight);

             }
		});

}