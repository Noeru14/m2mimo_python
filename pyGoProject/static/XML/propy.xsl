<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="utf-8" doctype-public="-//W3C//DTD HTML 4.01//EN" doctype-system="http://www.w3.org/TR/html4/strict.dtd"/>
<xsl:template match="/">

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>Règles du jeu de go</title>
</head>

	<h1><center><FONT color="blue"><xsl:value-of select="regles/titre"/></FONT></center></h1>

<body>
	<ul>
		<li>Materiel</li>
		<li>Chaines et libertes</li>
		<li>Territoires</li>
		<li>Deroulement du jeu</li>
		<li>Capture</li>
		<li>Vie et mort</li>
		<li>Répétitions</li>
		<li>Fin de la partie</li>
	</ul>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='1']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='1']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='2']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='2']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='3']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='3']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='4']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='4']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='5']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='5']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='6']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='6']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='7']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='7']/texte"/></p>
	
	<p><center><FONT color="blue"><b><xsl:value-of select="regles/regle[id='8']/nom" /></b></FONT></center></p>
	<p><xsl:value-of select="regles/regle[id='8']/texte"/></p>
	
	
</body>
</html>



</xsl:template>
</xsl:stylesheet>