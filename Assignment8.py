list = ["Abu Jayed","Ebadot Hossain","Liton Das","Mahmudullah","Mohammad Mithun","Mohammad Saifuddin"]
with open("mysquad.txt","w") as files:
	files.write("My favorite cricket team is : Bolda\n")

count=2
with open("mysquad.txt","a") as file:
	for i in range(0,6):
	#print(count,"==>",list[i])
		file.write(str(count)+" ==> "+list[i]+"\n")
		count+=2