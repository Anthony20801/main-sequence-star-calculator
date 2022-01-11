def read_data() -> object:
    f = open("HRdata",'r')
    Dic={}
    while True:
        line= f.readline()
        if not line: break
        Arr=line.split(" ")
        Dic[Arr[0]]=Arr[1:]

    f.close()
    return Dic

def make_datas():

    import sys
    f= open("HRdata",'a')

    while True:
        Name, C, L, T= sys.stdin.readline().split()
        YN=input("GO?")
        f.write(Name+" "+C+" "+L+" "+T+"\n")
        if YN=="N": break

    f.close()

# make_datas()
