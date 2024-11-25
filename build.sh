TARGET=target
TEX=paper.tex

rm -r $TARGET
mkdir $TARGET
cd $TARGET

pdflatex ../src/$TEX
pdflatex ../src/$TEX

mv paper.pdf ..
cd ..
open paper.pdf
