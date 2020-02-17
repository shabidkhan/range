def shabid(b,a=None,c=1):
	if a==None:
		a=0
	else:
		b,a=a,b
	list_=[]
	while(b>a and c>=0) or (b<a and c<0):
		list_+=[a]
		a+=c
	return list_
