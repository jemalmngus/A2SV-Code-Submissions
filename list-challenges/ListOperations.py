if __name__ == '__main__':
    N = int(input())
    g=[]
    for _ in range(N):
        x=input().split()
        if x[0]=="append":
            for i in range(1,len(x)):
                g.append(int(x[i]))
        elif x[0]=="print":
            print(g)
        elif x[0]=="insert":
            g.insert(int(x[1]),int(x[2]))
        elif x[0]=="remove":
            g.remove(int(x[1]))
        elif x[0]=="sort":
            g.sort()
        elif x[0]=="reverse":
            g.reverse()
        else:
            g.pop()
            
        
