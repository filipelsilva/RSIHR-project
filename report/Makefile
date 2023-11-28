LATEX=pdflatex
LATEXFLAGS=-shell-escape

sample-acmtog.pdf: sample-acmtog.tex
	pdflatex -shell-escape sample-acmtog.tex

.PHONY: refs
refs: sample-acmtog.aux
	bibtex sample-acmtog

.PHONY: clean
clean:
	find -type f -name 'sample-acmtog.*' -not -name 'sample-acmtog.tex' -delete
	rm -rf _minted-sample-acmtog

.PHONY: watch
watch:
	watchexec --exts tex make
