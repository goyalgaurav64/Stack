def createStack():
    s=[]
    return s

def push(s,li=[]):
    s.append(li)

def pop(s):
    return s.pop()

def top(s):
    n=len(s)
    return s[n-1]

def isEmpty(s):
    return len(s)==0

def CalSpan(a):
    n=len(a)
    v=[]
    s=createStack()
    for i in range(n):
        if isEmpty(s) is True:
            v.append(-1)
        elif isEmpty(s) is False and a[top(s)] >= a[i]:
            v.append(top(s))
        elif isEmpty(s) is False and a[top(s)] < a[i]:
            while isEmpty(s) is False and a[top(s)] < a[i]:
                pop(s)
            if isEmpty(s) is True:
                v.append(-1)
            else:
                v.append(top(s))
        push(s,i)
    
    for i in range(len(v)):
        v[i]=i-v[i]
    return v



if __name__ == "__main__":
    a=[100,80,60,70,60,75,85]
    ans=CalSpan(a)
    print(ans)