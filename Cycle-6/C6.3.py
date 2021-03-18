with open('D:\csv.csv','r') as f:
    f_contents=f.readlines()
    l=list(f_contents)
    print(l)
f.close()