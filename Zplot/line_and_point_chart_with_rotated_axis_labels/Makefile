PY=python
EPS2PDF=ps2pdf
CROP=pdfcrop

SRC = line_point_chart.py
EPS = $(patsubst %.py,%.eps,$(SRC))
PDF = $(patsubst %.py,%.pdf,$(SRC))

all: $(EPS) $(PDF)

%.eps: %.py
	$(PY) $< eps

%.pdf: %.eps
	$(EPS2PDF) $<
	$(CROP) $@ $@

fig:
	cp -f *.pdf ../../figure/	

clean: 
	rm -rf *.eps *.pdf
