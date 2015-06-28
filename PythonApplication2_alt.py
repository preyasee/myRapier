import csv
import matplotlib.pyplot as plt

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
	

		
f_obj.close()



Z1=map(lambda x:-x,Z)
tenor1=map(lambda x:float(x[:-1]),tenor)
temp = dict(zip(tenor1, carry_size))
from collections import Counter
#Counter(temp).most_common()
temp1=dict(zip(z_SVD, Z1))
filtered_temp1 = {k:v for (k,v) in temp1.items() if k != ""}


#fig, axes = plt.subplots(figsize=(12, 6))

fig, axes = plt.subplots(figsize=(12, 6))
axes.set_title("OutRights(rich/cheap)")
axes.set_xlim([-3.0,4.0])
axes.set_ylim([0,4.0])
axes.spines['bottom'].set_position(('data',0))
axes.spines['left'].set_position(('data',0))
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')
#axes[0].plot(z_SVD, Z1, color="blue", lw=2, ls='*', marker='s', alpha=0.8)
axes.plot(filtered_temp1.keys(), filtered_temp1.values(), color="blue", lw=2, ls='*', marker='s')
#axes.scatter(filtered_temp1.keys(), filtered_temp1.values(), color="blue", marker='s')

for aa,x,y in zip(levels,filtered_temp1.keys(),filtered_temp1.values()):
	axes.annotate(aa,xy=(x,y),fontsize=10)

fig.tight_layout()
fig.savefig("outrights1.svg",dpi=500)
	
fig, axes = plt.subplots(figsize=(12, 6))
axes.bar(tenor1,carry_sgn,width=0.5,color='r')
axes.bar(tenor1,rroll,width=0.5,color='y', bottom=carry_sgn)
ax2=axes.twinx()
#ax2.plot(tenor1,carry_size,lw=2,color="blue", ls='*', marker='s')
ax2.plot(temp.keys(),temp.values(),lw=2,color="blue")
ax2.set_ylabel("risk adj carry+roll", fontsize=14, color="red")

	
fig.tight_layout()
fig.savefig("outrights2.svg",dpi=500)
