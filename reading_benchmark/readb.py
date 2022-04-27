def main():
    for i in range(len(open_file())):
        print(i, '# ', get_list(open_file()[i]))
def open_file():
    path='benchmark\chubeas\OR5x100\OR5x100-0.25_1.dat'
    melef=open(path,"r")
    return melef.readlines()
def get_list(a):
    ra8m=0
    cap=[]
    for i in range(1, len(a)):
        if(a[i]==' '):
            cap.append(a[ra8m+1:i])
            ra8m=i
        if(i==len(a)-1):
            cap.append(a[ra8m+1:])
    if(cap[-1]=='\n'):cap.pop(-1)
    return cap
main()