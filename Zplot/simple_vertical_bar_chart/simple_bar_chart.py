#! /usr/bin/env python

import sys
sys.path.insert(0,'..')
from zplot import *

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='simple_bar_chart', dimensions=['340', '180'])

t = table(file='bar_chart_data.dat')

d = drawable(canvas=c,
             coord=[50,30],
             yrange=[0,216], 
             dimensions=[270, 110],
             xrange=[-0.6, t.getmax('rownumber')+0.6],
             )

axis(drawable=d, style='y',
     ytitle='Time (ms)',
     yauto=[0,216,50]
    )

axis(drawable=d, style='x',
     xtitle='Data Size (MiB)',
     xmanual=t.getaxislabels('dataSize')
     )

p = plotter()

L = legend()

grid(drawable=d, x=False, ystep=50, linecolor='lightgrey', yrange=[50, 200], linedash=[2,2])

p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield='baseLine',
               labelfield='baseLine',
               labelshift=[-4, 0],
               fill=True, fillcolor='white', barwidth=0.7, yloval=0,
               linewidth=0.5, cluster =[0,3], legend=L, legendtext="Base Line")

p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield='method1',
               labelfield='method1',
               fill=True, fillcolor='black', barwidth=0.7, yloval=0,
               fillstyle='dline2', fillsize=0.5, fillskip=4,
               linewidth=0.5, cluster =[1,3], legend=L, legendtext="Method #1")

p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield='method2',
               labelfield='method2',
               labelshift=[4, 0],
               fill=True, fillcolor='black', barwidth=0.7, yloval=0,
               fillstyle='hline', fillsize=0.5, fillskip=4,
               linewidth=0.5, cluster =[2,3], legend=L, legendtext="Method #2")

L.draw(c, coord=[d.left()+190, d.top()-2],
       width=8, height=8,
       skipnext=3, skipspace=100,
       vskip=5
       )

c.render()

