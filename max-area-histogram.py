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

def CanRectexpandOnRight(a):
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

def CanRectexpandOnLeft(a):
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

def findMaxAreaofRect(a):
    right=CanRectexpandOnRight(a)
    left=CanRectexpandOnLeft(a)
    width=[0]*len(a)
    res=-1
    for i in range(len(a)):
        width[i]=right[i]-left[i]-1
    
    for i in range(len(a)):
        res=max(res,a[i]*width[i])
    return res


if __name__ == "__main__":
    a=[6,2,5,4,5,1,6]
    # a=[2,1,5,6,2,3]
    # a=[2,3,4,2]
    # a=[3,4,3,2]
    ans=findMaxAreaofRect(a)
    print("Max area of rect can be:",ans)