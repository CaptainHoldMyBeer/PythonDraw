
def C(w,h):
    mas=[]
    if(w>0 and h > 0):
        for i in range(h+2):
            mas.append([])
            for j in range(w+2):
                mas[i].append(" ")
    
        for i in range(h+2):
            mas[i][0]="|"
            mas[i][w+1]="|"
        for i in range(w+2):
            mas[0][i]="-"
            mas[h+1][i]="-"
    return mas


def L(x1,y1,x2,y2,mas):
    if(x1>0 and x2>0 and y1>0 and y2>0):
        if(y1==y2):
            for i in range(x1,x2+1,1):
                mas[y1][i]="x"

        if(x1==x2):
            for i in range(y1,y2+1,1):
                mas[i][x1]="x"
     
    return mas

def R(x1,y1,x2,y2,mas):
    if(x1>0 and x2>0 and y1>0 and y2>0):
        for i in range(x1,x2+1,1):
            mas[y1][i]="x"
            mas[y2][i]="x"
        for i in range(y1,y2+1,1):
            mas[i][x1]="x"
            mas[i][x2]="x"

    return mas


def Fill_lineH(x,y,c,mas):
    i=y
    while(i>=1 and mas[x][i]!="x"):
        mas[x][i]=c
        i-=1
        
    i=y
    while(i<len(mas[0])-1 and mas[x][i]!="x"):
        mas[x][i]=c
        i+=1
        
    return mas


def Fill_lineV(x,y,c,mas):
    i=x
    while(i>=1 and mas[i][y]!="x"):
        mas[i][y]=c
        i-=1
        
    i=x
    while(i<len(mas)-1 and mas[i][y]!="x"):
        mas[i][y]=c
        i+=1
        
    return mas

def B(x,y,c,mas):
    if(x>0 and y>0):
        if(mas[x][y]!="x"):
            i=x
            while(i>=1 and mas[i][y]!="x"):
                Fill_lineH(i,y,c,mas)
                i-=1
            
            i=x
            while(i<len(mas)-1 and mas[i][y]!="x"):
                Fill_lineH(i,y,c,mas)
                i+=1
        
            i=y
            while(i>=1 and mas[x][i]!="x"):
                Fill_lineV(x,i,c,mas)
                i-=1
            
            i=y
            while(i<len(mas)-1 and mas[x][i]!="x"):
                Fill_lineV(x,i,c,mas)
                i+=1
        
    return mas  



def Show(mas):
    for i in range(len(mas)):
        for j in range(len(mas[0])):
            print(mas[i][j],end="")
        print("\n")



def Draw(path):
    f = open(path)
    lines=[]
    mas = []
    
    for line in f:
        tmp = line
        lines.append(tmp.split(" "))

    if(lines[0][0]!="C"):
              print("Необходимо задать размер окна!")
    else:
        for i in range(len(lines)):
       
            if(lines[i][0]=="C"):
                  mas=C(int(lines[i][1]),int(lines[i][2]))
              
            if(lines[i][0]=="L"):
                  L(int(lines[i][1]),int(lines[i][2]),int(lines[i][3]),int(lines[i][4]),mas)

            if(lines[i][0]=="R"): 
                  R(int(lines[i][1]),int(lines[i][2]),int(lines[i][3]),int(lines[i][4]),mas)

            if(lines[i][0]=="B"): 
                  B(int(lines[i][2]),int(lines[i][1]),str(lines[i][3]),mas)

    Show(mas)
   
    

Draw("input.txt")

    


