#Cartesian product

lst_1=[1,2,3]
lst_2=[4]
lst_3=[]
tmp_lst=[]
fnl_lst=[]
lst_4=[5,6]
lst_5=[]

for i in zip(lst_1):
	lst_3.append(list(zip(i,lst_2)))


for el in lst_3:
	for i in el:
		tmp_lst.append(i)


for i in zip(tmp_lst):
	for j in zip(lst_4):
		lst_5.append(list(zip(i,j)))
#print(lst_5)

for el in lst_5:
	#print(el)
	for i in el:
		fnl_lst.append(i)
print(fnl_lst)

		
