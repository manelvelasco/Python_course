#!/bin/bash
Pweave -c --cache-directory=cache --figure-directory=plwfigis -f texminted       $1.Plw &&                                                          
#Pweave -c --cache-directory=cache --figure-directory=plwfigis -f texminted  -g png   $1.Plw && 

#read -p "Mira quin error més maco t'ha sortit." &&
sed 's/mathescape/bgcolor=mybg,frame=lines,mathescape/' $1.tex > $1.otex && 
mv $1.otex $1.tex && 
sed 's/.png//' $1.tex > $1.otex && 
 mv $1.otex $1.tex && 
pdflatex  -synctex=1 -shell-escape $1 
#&& pdflatex -shell-escape $1


