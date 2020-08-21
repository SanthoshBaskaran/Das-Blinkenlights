Time = list(map(int,input().split()))
light1=[]
blow=Time[0]
blow2=Time[1]
for i in range(Time[2]):
    light1.append(0)
light2=light1.copy()
j=blow-1
while(j<=len(light1)-1):
    light1[j]=1
    j=j+blow
k=blow2-1
while(k<=len(light2)-1):
    light2[k]=1
    k=k+blow2
result_analysis=0
q=0
while(q<=len(light1)-1):
    if((light1[q] and light2[q])==1):
        result_analysis=result_analysis+1
    else:
        result_analysis=result_analysis+0
    q=q+1
if(result_analysis<=0):
    print('no')
else:
    print('yes')
    
