doc = main
all: main.pdf
main.pdf: $(doc).tex
	pdflatex $(doc)
	pdflatex $(doc)
	rm -f *.aux *.log *.nav *.out *.snm *.toc *~ *.backup

bib: $(doc).tex
	pdflatex $(doc)
	bibtex $(doc)
	pdflatex $(doc)
	pdflatex $(doc)
clean:
	rm −f *.aux *.log *.nav *.out *.snm *.toc *~ *.backup *.bbl *.blg *.pdf
