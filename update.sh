cp -r ./src/* ./target/

cd target

pdflatex paper.tex
mv paper.pdf ..
