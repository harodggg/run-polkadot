ll = []
filters = []
b = 0
fo = open("foo.txt", "w")

for f in open("filter.txt","r"): 
	ll.append(f.strip())


for i in range(0,2000):
	if int(ll[b]) == int(ll[b+1]):
		print("1")
		
	elif int(ll[b+1]) == int(ll[b+2]):
		print("2")
		fo.write(ll[b]+"\n")
		b = b + 1 
	
	else:
		fo.write(ll[b] + "\n")
		fo.write(ll[b+1] + "\n")

	b = b + 2


		
fo.close()
		
	
