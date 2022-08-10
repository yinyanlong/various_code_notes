.Phony:: all view 

all: pdf

pdf: main.tex
	xelatex -shell-escape main
	xelatex -shell-escape main

clean:
	rm main.aux main.log

view:
	xdg-open main.pdf

