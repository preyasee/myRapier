import matplotlib.pyplot as plt
import collections
import numpy as np
import csv
import math
import pylab

def mapcolor(elem):
	temp=math.copysign(1,elem)
	if temp == 1:
		return 'g'
	else:
		return 'r'
	
		



type1 =[];
type2 =[];
tenor =[];
carry_sgn=[];
carry_size=[];
carry =[];
sgn =[];


f_obj = open("bubbledata.csv");
reader=csv.DictReader(f_obj,delimiter=',');
for line in reader:
    type1.append(float(line["Corr_PC1"]))
    type2.append(float(line["Corr_PC2"]))
    tenor.append(line["PT_Tenor1"]+line["PT_Tenor2"]+line["PT_Tenor3"])
    carry_sgn.append(float(line["Carry(3m)"]))
    carry_size.append(float(line["(Carry+Roll)/Std"]))
    
    

carry = map(lambda elem: 400*abs(elem), carry_size)
#sgn = map(lambda elem:math.copysign(1,elem), carry_sgn)
sgn = map(lambda elem:mapcolor(elem), carry_sgn)

fig=plt.figure()
axes1 =fig.add_axes([0,0,1,1])
axes2 = fig.add_axes([0.08,0.1,0.85,0.85], frameon=True,alpha=0)
axes1.set_xlim(xmin=-1, xmax=1)
axes1.set_ylim(ymin=-1, ymax=1)
axes1.annotate('Bull',(-0.5,-0.9))
axes1.annotate('Bear',(0.5,-0.9))
axes1.annotate('Bull',(-0.5,0.92))
axes1.annotate('Bear',(0.5,0.92))
axes1.annotate('Steepener',(-0.95,0.5),rotation=90)
axes1.annotate('Flattener',(-0.95,-0.5),rotation=90)
axes1.annotate('Steepener',(0.90,0.5),rotation=270)
axes1.annotate('Flattener',(0.90,-0.5),rotation=270)
axes1.axis('off')

axes2.set_xlim(xmin=-1, xmax=1)
axes2.set_ylim(ymin=-1, ymax=1)
axes2.spines['right'].set_color('none')
axes2.spines['top'].set_color('none')
axes2.xaxis.set_ticks_position('bottom')
axes2.spines['bottom'].set_position(('data',0)) 
axes2.yaxis.set_ticks_position('left')
axes2.spines['left'].set_position(('data',0))   
axes2.scatter(type1,type2,s=carry,marker='o',c=sgn,alpha=0.75)

for aa,x,y in zip(tenor,type1,type2):
	axes2.annotate(aa,xy=(x,y),fontsize=10)

fig.savefig("bubbleplot.svg", dpi=500)
