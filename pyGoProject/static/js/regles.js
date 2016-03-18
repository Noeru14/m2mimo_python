/* ! ne fonctionne pas
fonction pour appeler les règles en XML */

function regles(){
	$("body").css("background-color", "#b2beb5");
	this.div = document.createElement("div");
	this.div.className = "welDiv";
	this.div.id= "Div_XML";

	this.title = document.createElement("h3");
	this.title.innerHTML = "Règles";
	this.title.className = "welTitle";
	this.title.id = "titleID";

	this.div.appendChild(this.title);

	$("body").html(this.div);
	$(document).ready(
 function()
 {
   $.ajax( {
			type: "GET",
			url: "static/XML/projet.xml",
			dataType: "xml",
			success: function(xml)
					 {
					   $(xml).find('regle').each(
						 function()
						 {
							var id = $(this).attr('id');
							var title = $(this).find('nom').text();
							var texte = $(this).find('texte').text();
							var id = $(this).find('id').text();
							$('<br><br><div class="items" id="' + id + '"></div>').html('<h3>' + title + '</h3>').appendTo('#Div_XML');



							$(this).find('texte').each(
											function()
											{
												var long = $(this).text();

												$('<p class=""></p>').html(long).appendTo('#'+id);

											});
						  });
					    this.backBtn = document.createElement("a");
                        this.backBtn.innerHTML = "Retour";
                        this.backBtn.href = "";
                        this.backBtn.className = "welBtn button button-circle button-flat-highlight";
                        $(".welDiv").append(this.backBtn);


					  }
		});


  })

};





