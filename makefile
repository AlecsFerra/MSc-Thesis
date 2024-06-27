all: compile

compile:
	latexmk -pdflatex='pdflatex -file-line-error -synctex=1' -outdir=out -auxdir=aux -pdf thesis.tex
	python3 flatten.py thesis.tex flat.tex
	latexmk -pdflatex='pdflatex -file-line-error -synctex=1' -outdir=out -auxdir=aux -pdf flat.tex
clean:
	rm -rf aux out
