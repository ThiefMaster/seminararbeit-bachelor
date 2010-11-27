NAME=Seminararbeit
ARGS=-shell-escape -interaction=nonstopmode
SRC=$(wildcard *.tex)

pdf:
	@echo Building PDF
	@pdflatex $(ARGS) -draftmode $(NAME).tex
	@pdflatex $(ARGS) $(NAME).tex

clean:
	@echo Cleaning up
	@rm -f $(NAME).pdf *.aux *.log *.out *.toc *.pyg
