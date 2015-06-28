import matplotlib.pyplot as plt
import collections
import numpy as np
import csv
import math
import pylab




f_obj = open("noRegression.csv");
reader=csv.DictReader(f_obj,delimiter=',');

type1 =[];
type2 =[];
tenor =[];
carry_sgn=[];
carry_size=[];
carry =[];
sgn =[];
Level_High=[];
Level_Low=[];
Level_Current=[];
z_SVD=[];
Z=[];
rroll=[];
levels=[];
std=[];

f=lambda x: 0 if (x == "") else x

for line in reader:
    if (line["PT_Currency"] in "USD" and line["Main Product Type"] in "swap" and line["PT Name"] in "outright"):
		print (line["Level_Current"])
		type1.append(float(line["Corr_PC1"]))
		type2.append(float(line["Corr_PC2"]))
		tenor.append(line["PT_Tenor1"]+line["PT_Tenor2"]+line["PT_Tenor3"])
		carry_sgn.append(float(line["Carry(3m)"]))
		carry_size.append(float(line["(Carry+Roll)/Std"]))
		Z.append(float(f(line["Z"])))		
		z_SVD.append(line["Z_SVD"])
		Level_Current.append(float(line["Level_Current"]))
		Level_High.append(float(line["Level_High(3m)"]))
		Level_Low.append(float(line["Level_Low(3m)"]))
		levels.append("(C:" + str(round(float(line["Level_Current"]),2)) + ",L:" + str(round(float(line["Level_Low(3m)"]),2)) + ",H:" + str(round(float(line["Level_High(3m)"]),2)) + ")")
		rroll.append(float(line["Roll(3m)"]))	
		std.append(float(line["Std"]))
	

		
f_obj.close()



Z1=map(lambda x:-x,Z)
tenor1=map(lambda x:float(x[:-1]),tenor)
temp = dict(zip(tenor1, carry_size))
from collections import Counter
#Counter(temp).most_common()
temp1=dict(zip(z_SVD, Z1))
filtered_temp1 = {k:v for (k,v) in temp1.items() if k != ""}

asd=np.array([tenor,Level_Current,Level_Low, Level_High, carry_sgn, rroll, std,Z])
cellText1=asd.T
colLabels1 = ('Outrights', 'Lvl', 'Lvl Low', 'Level_High', 'Carry', 'Roll', 'Daily vol', 'Z PCA')
#rowLabels1 = ['%d year' % x for x in (100, 50, 20, 10, 5)]
#colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rowLabels1)))
fig, ax = plt.subplots()
ax.table(cellText=cellText1[0:10],colLabels=colLabels1, loc='center')
#ax.table(cellText=cellText1,colLabels=colLabels1, loc='center',rowLabels=rowLabels1,rowColors=colors)
ax.axis('off')
fig.savefig("table1.pdf",dpi=500,bbox_inches='tight')




