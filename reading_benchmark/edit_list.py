def edit(dat):
    ra8m=0
    cap=[]
    for i in range(1, len(dat)):
        if(dat[i]==' '):
            cap.append(dat[ra8m+1: i])
            ra8m=i
        if(i==len(dat)-1):
            cap.append(dat[ra8m+1:])
    return cap