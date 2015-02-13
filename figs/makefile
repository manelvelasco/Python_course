# Makefile for batch conversion of .svg to .eps

IMAGES=${patsubst %.svg,%.pdf,${wildcard *.svg}}

%.pdf : %.svg
	@inkscape -D -T -E $(<:.svg=.pdf) -f $<

svg: $(IMAGES)
