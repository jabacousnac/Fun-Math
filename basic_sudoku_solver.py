from datetime import datetime
start_time = datetime.now()

def looper(square):
    bag=[1,2,3,4,5,6,7,8,9]
    new=bag
    remover=[]
    final=[]
    for r in range(len(square)):
        for c in range(len(square[r])):
            if r%3==0 and c%3==0 and square[r][c]==0:#1 in mini square
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:#check row
                            remover+=[i]                    
                        elif i==square[j-1][c]:#check column
                            remover+=[i]
                        elif i==square[r+1][c+1] or i==square[r+1][c+2] or i==square[r+2][c+1] or i==square[r+2][c+2]:#check rest of minisquare
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #2 in mini square        
            elif r%3==0 and (c-1)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r+1][c-1] or i==square[r+2][c-1] or i==square[r+1][c+1] or i==square[r+2][c+1]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c, ',',len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #3 in mini square        
            elif r%3==0 and (c-2)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r+1][c-2] or i==square[r+1][c-1] or i==square[r+2][c-2] or i==square[r+2][c-1]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #4 in mini square        
            elif (r-1)%3==0 and c%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c+1] or i==square[r-1][c+2] or i==square[r+1][c+1] or i==square[r+1][c+2]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #5 in mini square        
            elif (r-1)%3==0 and (c-1)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c-1] or i==square[r+1][c+1] or i==square[r-1][c+1] or i==square[r+1][c-1]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #6 in mini square        
            elif (r-1)%3==0 and (c-2)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c-1] or i==square[r-1][c-2] or i==square[r+1][c-1] or i==square[r+1][c-2]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]  
                    final=[]
                else:
                    final=[]
            ### #7 in mini square        
            elif (r-2)%3==0 and c%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c+1] or i==square[r-1][c+2] or i==square[r-2][c+1] or i==square[r-2][c+2]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #8 in mini square        
            elif (r-2)%3==0 and (c-1)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c+1] or i==square[r-1][c-1] or i==square[r-2][c+1] or i==square[r-2][c-1]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',',len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
            ### #9 in mini square        
            elif (r-2)%3==0 and (c-2)%3==0 and square[r][c]==0:
                remover=[]
                for i in new:
                    for j in bag:
                        if i in square[r]:
                            remover+=[i]                    
                        elif i==square[j-1][c]:
                            remover+=[i]
                        elif i==square[r-1][c-1] or i==square[r-1][c-2] or i==square[r-2][c-1] or i==square[r-2][c-2]:
                            remover+=[i]
                        else:
                            new=new
                for num in bag:
                    if num not in remover:
                        final.append(num)
                print r,c,',', len(final)
                if len(final)==1:
                    square[r][c]=final[0]
                    final=[]
                else:
                    final=[]
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    return square

def filled(square):
    L=[]
    for i in square:
        for j in i:
            L.append(j)
    if 0 in L:
        return False
    else:
        return True
    
def ss(square):
    while filled(square)==False:
        looper(square)
    return square


    

            
square1=[[0,0,6,2,0,0,9,0,0],[0,0,0,6,0,9,0,0,0],[0,5,0,0,0,7,0,0,1],[0,0,0,0,0,0,8,0,7],[0,2,1,0,8,0,3,4,0],[3,0,8,0,0,0,0,0,0],[7,0,0,9,0,0,0,2,0],[0,0,0,1,0,3,0,0,0],[0,0,3,0,0,8,5,0,0]]

square2=[[0,0,2,0,0,0,5,0,0],[0,7,0,1,0,5,0,2,0],[3,5,0,0,0,0,0,6,7],[5,0,0,0,7,0,0,0,8],[0,2,0,4,9,3,0,1,0],[4,0,0,0,5,0,0,0,9],[6,3,0,0,0,0,0,4,1],[0,4,0,7,0,6,0,9,0],[0,0,7,0,0,0,3,0,0]]
