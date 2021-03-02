

a=[[1,2],[3,5],[6,7],[8,10],[12,16]]
m=[4,9]
res=[]

def mergeIntervals(a,m):
    for i in range(len(a)):
        if a[i][1] < m[0]:
            a.append(a[i])
        elif a[i][0] > m[1]:
            res.append(m)
            return res + a[i:]
        else:
            m[0]=min(a[i][0],m[0])
            m[1]=max(a[i][1],m[1])
        res.append(m)
    print(res)

print(mergeIntervals(a,m))
