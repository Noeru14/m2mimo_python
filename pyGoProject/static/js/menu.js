/* le menu qui apparait en front */
function menu(){
    $("body").css("background-color", "#b2beb5");
    this.div = document.createElement("div");
    this.div.className = "welDiv";

	this.title = document.createElement("p");
    this.title.innerHTML = "Jeu de GO";
    this.title.className = "welTitle";
    
	this.title1 = document.createElement("p");
    this.title1.innerHTML = "Jacques Hovine, Jean-Philippe Persici, William Ung";
    this.title1.className = "welC"; 

    this.form = document.createElement("form"); 
    this.form.className = "welFrom form-inline";

	this.enterBtn = document.createElement("a");
    this.enterBtn.innerHTML = "Jouer";
    this.enterBtn.href = "#";
    this.enterBtn.className = "welBtn button button-circle button-flat-highlight";
    $(this.enterBtn).hide();
    
	this.scoreBtn = document.createElement("a");
    this.scoreBtn.innerHTML = "Score";
    this.scoreBtn.href = "#";
    this.scoreBtn.className = "welBtn button button-circle button-flat-highlight";
    $(this.scoreBtn).hide();
    
    this.reglesBtn = document.createElement("a");
    this.reglesBtn.innerHTML = "Règles";
    this.reglesBtn.href = "#";
    this.reglesBtn.className = "welBtn button button-circle button-flat-highlight";
    $(this.reglesBtn).hide();

    //$("body").append(this.title);
    this.div.appendChild(this.title);
    this.div.appendChild(this.title1);
    this.div.appendChild(this.form);
    this.div.appendChild(this.enterBtn);
    this.div.appendChild(this.scoreBtn);
    this.div.appendChild(this.reglesBtn);
    $("body").append(this.div);

    this.showTitle = function(){
        $(".welTitle").css("font-size", "1px");
        $(".welTitle").animate({
            fontSize: '90px' 
        }, 1000);
    };
    
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

  // renvoi vers jouer
  this.goAway1 = function(){
            
        $(".welDiv").animate({
            margin: '50px',
            opacity: '0'
        }, 1000);
        setTimeout("$('.welDiv').remove()", 1000);

        setTimeout("jouer()", 1000);
    };
    
  // renvoi vers score
  this.goAway2 = function(){
            
        $(".welDiv").animate({
            margin: '50px',
            opacity: '0'
        }, 1000);
        setTimeout("$('.welDiv').remove()", 1000);

        setTimeout("score()", 1000);
    };

  // renvoi vers regles
  this.goAway3 = function(){
            
        $(".welDiv").animate({
            margin: '50px',
            opacity: '0'
        }, 1000);
        setTimeout("$('.welDiv').remove()", 1000);

        setTimeout("regles()", 1000);
    };
    
	// boutons de renvoi vers les differentes pages : jouer, regles ou scores
	this.enterBtn.addEventListener("click", this.goAway1);
	this.scoreBtn.addEventListener("click", this.goAway2);
	this.reglesBtn.addEventListener("click", this.goAway3);

}



