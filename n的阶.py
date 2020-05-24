#encoding:utf-8
import sys
import datetime
start = datetime.datetime.now()
savedStdout = sys.stdout
file=open('out.txt', 'w+')
sys.stdout = file
N=10000
M=[2]
S=[]
value=[]
length=1 
for i in range(0,N+1):
    value.append(1)
for i in range(2,N):
    flag=0
    for j in M:
        if i%j==0:
            flag=1
    if flag==0:
            M.append(i)
            length=length+1
v = [[0 for i in range(N)] for i in range(N)]
for i in range(0,length):
    j=0
    while pow(M[i],j+1)<=N:
        v[i][j]=pow(M[i],j+1)
        j=j+1
    S.append(j)
for i in range(0,length):
    for j in range(N,0,-1):
        for k in range(0,S[i]):
            if j>=v[i][k]:
                    value[j] = max(value[j],value[j - v[i][k]]*v[i][k])
for i in range(1,N):
    print(value[i])
file.close()
sys.stdout = savedStdout
end = datetime.datetime.now()
print ("运行时间为:",end-start)