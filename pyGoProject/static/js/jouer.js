/* fonction dans le menu pour creer la partie de jeu */
function jouer(){
    $("body").css("background-color", "#b2beb5");
    this.div = document.createElement("div");
    this.div.className = "welDiv";

    this.form = document.createElement("form"); 
    this.form.className = "welFrom form-inline";
    
    // joueur 1
    this.nameInput1 = document.createElement("input");
    this.nameInput1.type = "text";
    this.nameInput1.id = "player1";
    this.nameInput1.placeholder="Joueur 1";
    this.nameInput1.className = "welInput";

	// joueur 2
    this.nameInput2 = document.createElement("input");
    this.nameInput2.type = "text";
    this.nameInput2.id = "player2";
    this.nameInput2.placeholder="Joueur 2";
    this.nameInput2.className = "welInput";
    
    // nom de la partie
    this.nameInput3 = document.createElement("input");
    this.nameInput3.type = "text";
    this.nameInput3.id = "partyName";
    this.nameInput3.placeholder="Nom de la partie";
    this.nameInput3.className = "welInput";
    
    this.form.appendChild(this.nameInput1);
    this.form.appendChild(this.nameInput2);
    this.form.appendChild(this.nameInput3);
    $(this.form).css("padding-left", "800px");
    $(this.form).css("opacity", "0");

    this.enterBtn = document.createElement("a");
    this.enterBtn.innerHTML = "Jouer";
    this.enterBtn.href = "#";
    this.enterBtn.className = "welBtn button button-circle button-flat-highlight";
    $(this.enterBtn).hide();

    this.div.appendChild(this.form);
    this.div.appendChild(this.enterBtn);
    $("body").append(this.div);

    setTimeout(this.showTitle, 0);

    this.showBtn = function(){
        $(".welBtn").fadeIn(1000);
    };
    setTimeout(this.showBtn, 1000);

    this.showForm = function(){
        $(".welFrom").animate({
            opacity: '1',
            paddingLeft: '0px'
        }, 1000);    
    };
    setTimeout(this.showForm, 500);

	// recuperer le nom partie
    this.goAway = function(){
        if(document.getElementById("player1").value.trim()!="")
            NAMEPLAYER[0] = document.getElementById("player1").value.trim();
        if(document.getElementById("player2").value.trim()!="")
            NAMEPLAYER[1] = document.getElementById("player2").value.trim();
        if(document.getElementById("partyName").value.trim()!="")
            PARTYNAME = document.getElementById("partyName").value.trim();

        if(NAMEPLAYER[0]==NAMEPLAYER[1])
        {   alert("les noms des joueurs est le meme");
            return;
        }
        $(".welDiv").animate({
            margin: '50px',
            opacity: '0'
        }, 1000);
        setTimeout("$('.welDiv').remove()", 1000);

        setTimeout("begin()", 1000);
    };

    this.enterBtn.addEventListener("click", this.goAway);  
}