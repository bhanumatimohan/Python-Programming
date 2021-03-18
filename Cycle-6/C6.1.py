with open('D:\\file.txt','r') as f:
    x=[]
    f_contents=f.read()
    x.append(f_contents)
    print(x)
f.close()