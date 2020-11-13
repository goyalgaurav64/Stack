def createStack():
    s=[]
    return s

def push(s,ele):
    s.append(ele)

def pop(s):
    return s.pop()

def top(s):
    n=len(s)
    return s[n-1]

def isEmpty(s):
    return len(s)==0

def NSR(a):
    right=[]
    s=createStack()
    n=len(a)
    for i in range(n-1,-1,-1):
        if isEmpty(s) is True:
            right.append(n)
        elif isEmpty(s) is False and a[top(s)] < a[i]:
            right.append(top(s))
        elif isEmpty(s) is False and a[top(s)] >= a[i]:
            while isEmpty(s) is False and a[top(s)] >= a[i]:
                pop(s)
            if isEmpty(s) is True:
                right.append(n)
            else:
                right.append(top(s))
        push(s,i)
    return right[::-1]

def NSL(a):
    left=[]
    s=createStack()
    n=len(a)
    for i in range(n):
        if isEmpty(s) is True:
            left.append(-1)
        elif isEmpty(s) is False and a[top(s)] < a[i]:
            left.append(top(s))
        elif isEmpty(s) is False and a[top(s)] >= a[i]:
            while isEmpty(s) is False and a[top(s)] >= a[i]:
                pop(s)
            if isEmpty(s) is True:
                left.append(-1)
            else:
                left.append(top(s))
        push(s,i)
    return left 


def MAH(a):
    # for i in range(len(ar)):
    #     if ar[i]==0:
    #         a[i]=0
    #     else:
    #         a[i]=a[i]+ar[i]
    left=NSL(a)
    right=NSR(a)
    width=[0]*len(a)
    res=-1
    for i in range(len(a)):
        width[i]=right[i]-left[i]-1
    for i in range(len(a)):
        res=max(res,width[i]*a[i])
    return res


def MaxAreaBinaryRect(a):
    n=len(a)
    m=len(a[0])
    v=[0]*m
    res=-1
    for i in range(m):
        v[i]=a[0][i]
    print(v)
    res=MAH(v)
    for i in range(1,n):
        for j in range(m):
            if a[i][j]==0:
                v[j]=0
            else:
                v[j] += a[i][j]
        print(v)
        res=max(res,MAH(v))
    return res


if __name__ == "__main__":
    a=[[0,1,1,0],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,0,0]]
    ans=MaxAreaBinaryRect(a)
    print("Max area in Binary rectangle is:",ans)