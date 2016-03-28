abc=pd.read_csv("FwdSeries_transposed.csv", index_col=0)
for i in range(0,89):
    abc[[i]].to_csv('my_csv.csv', mode='a', header=False)		
	
	
cols=abc.columns.values


import csv

header=['Run', 'Expt', 'Speed']

with open('myfile.csv','w') as f:
    for sublist in header:
        f.write(sublist + ',')
    f.write('\n')
		

df2=abc.stack()
df2.to_csv('myfile.csv', header=False, mode='a')


	
