TARGET=target
TEXFILE=paper
BIB=my.bib

rm -r $TARGET
mkdir $TARGET
cd $TARGET

cp -r ../src/* .

pdflatex $TEXFILE.tex
bibtex $TEXFILE
pdflatex $TEXFILE.tex
pdflatex $TEXFILE.tex

mv paper.pdf ..
cd ..
