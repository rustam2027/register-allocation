TARGET=target
TEX=paper.tex

rm -r $TARGET
mkdir $TARGET
cd $TARGET

pdflatex ../src/$TEX
pdflatex ../src/$TEX

open paper.pdf
cd ..
