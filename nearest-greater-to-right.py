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


def NearestGreatertoRight(a):
    n=len(a)
    s=createStack()
    v=[]
    for i in range(n-1,-1,-1):
        if isEmpty(s) is True:
            v.append(-1)
        elif isEmpty(s) is False and top(s) > a[i]:
            v.append(top(s))
        elif isEmpty(s) is False and top(s) <= a[i]:
            while isEmpty(s) is False and top(s) <= a[i]:
                pop(s)
            if isEmpty(s) is True:
                v.append(-1)
            else:
                v.append(top(s))
        push(s,a[i])
        # print(s)
    return v[::-1] 



if __name__ == "__main__":
    # a=[1,3,2,4]
    a=[17,18,5,4,6,1]
    ans=NearestGreatertoRight(a)
    print("Greatest elements corresponding to every element is:",ans)