def swapfiledata():
    filename1= input('enter filename1  :  ')
    filename2= input('enter filename2  :  ')
    with open (filename1,'r') as a :
        data1=a.read()

    with open (filename2,'r') as b :
        data2=b.read()

    with open (filename1,'w') as a :
        a.write(data2)

    with open (filename2,'w') as b :
        b.write(data1)

swapfiledata()
    
    