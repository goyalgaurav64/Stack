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


def NearestSmallerToLeft(a):
    s=createStack()
    v=[]
    n=len(a)
    for i in range(n):
        if isEmpty(s) is True:
            v.append(-1)
        elif isEmpty(s) is False and top(s) < a[i]:
            v.append(top(s))
        elif isEmpty(s) is False and top(s) >= a[i]:
            while isEmpty(s) is False and top(s) >= a[i]:
                pop(s)
            if isEmpty(s) is True:
                v.append(-1)
            else:
                v.append(top(s))
        push(s,a[i])
    return v




if __name__ == "__main__":
    # a=[1,3,2,4]
    a=[11,13,21,3]
    ans=NearestSmallerToLeft(a)
    print("Nearest smallest to left:",ans)