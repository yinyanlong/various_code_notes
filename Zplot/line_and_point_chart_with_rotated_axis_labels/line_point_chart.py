#! /usr/bin/env python

import sys
sys.path.insert(0,'..')
from zplot import *

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='line_point_chart', dimensions=[380, 230])

t = table(file='line_point_chart.dat')

d = drawable(canvas=c,
             coord=[50,60],
             yrange=[0,2000],
             dimensions=[310, 100],
             xrange=[-0.5, t.getmax('rownumber')+0.5],
             )

axis(drawable=d, style='y',
     ytitle='Bandwidth (MiB/s)',
     yauto=[0, 2005, 500]
    )

axis(drawable=d, style='x',
     xtitle='Data Size',
     xmanual=t.getaxislabels('dataSize'),
     xlabelrotate=45,
     xlabelanchor='r,c',
     xtitleshift=[0, -20]
     )

p = plotter()

L = legend()

grid(drawable=d, x=False, ystep=500, linecolor='lightgrey', yrange=[500,2000], linedash=[2,2])

POINT_SIZE=3

p.line(d, t, xfield='rownumber', yfield='method1',
         symbstyle='triangle',
         symbsize=POINT_SIZE, linewidth=1)
p.points(d, t, xfield='rownumber', yfield='method1',
         style='triangle',
         size=POINT_SIZE, linewidth=1,
         legend=L, legendtext='Method #1')

p.line(d, t, xfield='rownumber', yfield='method2',
         symbstyle='square',
         symbsize=POINT_SIZE, linewidth=1)
p.points(d, t, xfield='rownumber', yfield='method2',
         style='square',
         size=POINT_SIZE, linewidth=1,
         legend=L, legendtext='Method #2')
		 
L.draw(c, coord=[d.left()+15, d.top()-6],
       width=7, height=7,
       skipnext=3, skipspace=120,
       vskip=5
       )

c.render()

